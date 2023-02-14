from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect
from pydantic import BaseModel
import asyncio
from broadcaster import Broadcast
from fastapi import APIRouter


router = APIRouter(prefix='/api')

broadcast = Broadcast("redis://localhost:6379")
CHANNEL = "CHAT"


class MessageEvent(BaseModel):
    message: str


@router.on_event("startup")
async def startup():
    await broadcast.connect()


@router.on_event("shutdown")
async def shutdown():
    await broadcast.disconnect()


async def receive_message(websocket: WebSocket):
    async with broadcast.subscribe(channel=CHANNEL) as subscriber:
        async for event in subscriber:
            message_event = MessageEvent.parse_raw(event.message)
            await websocket.send_text("".join(message_event.dict().values()))


async def echo_message(websocket: WebSocket):
    data = await websocket.receive_text()
    event = MessageEvent(message=data)
    await broadcast.publish(channel=CHANNEL, message=event.json())


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    try:
        while True:
            receive_message_task = asyncio.create_task(
                receive_message(websocket))
            echo_message_task = asyncio.create_task(
                echo_message(websocket))
            done, pending = await asyncio.wait(
                {echo_message_task, receive_message_task}, return_when=asyncio.FIRST_COMPLETED)

            [task.cancel() for task in pending]
            [task.result() for task in done]

    except WebSocketDisconnect:
        await websocket.close()
