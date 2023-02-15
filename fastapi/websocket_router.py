from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect
from pydantic import BaseModel
import asyncio
from broadcaster import Broadcast
from fastapi import APIRouter
import json


router = APIRouter(prefix='/api')

broadcast = Broadcast("redis://localhost:6379")
CHANNEL = "ch01"


class MessageEvent(BaseModel):
    senduser: str
    username: str
    team: str
    message: str


@router.on_event("startup")
async def startup():
    await broadcast.connect()


@router.on_event("shutdown")
async def shutdown():
    await broadcast.disconnect()


async def receive_message(websocket: WebSocket, username: str, team: str):
    async with broadcast.subscribe(channel=CHANNEL) as subscriber:
        async for event in subscriber:
            message_event = MessageEvent.parse_raw(event.message)
            if message_event.username == username or message_event.team == team:
                await websocket.send_text("".join(message_event.json()))


async def echo_message(websocket: WebSocket, username: str, team: str):
    print(username)
    data = await websocket.receive_text()
    data = json.loads(data)

    event = MessageEvent(
        message=data['message'], username=data["username"], team=data["team"], senduser=username)

    await broadcast.publish(channel=CHANNEL, message=event.json())


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str = 'sender', team: str = 'all'):
    await websocket.accept()

    try:
        while True:
            receive_message_task = asyncio.create_task(
                receive_message(websocket, username=username, team=team))
            echo_message_task = asyncio.create_task(
                echo_message(websocket, username=username, team=team))
            done, pending = await asyncio.wait(
                {echo_message_task, receive_message_task}, return_when=asyncio.FIRST_COMPLETED)

            [task.cancel() for task in pending]
            [task.result() for task in done]

    except WebSocketDisconnect:
        await websocket.close()
