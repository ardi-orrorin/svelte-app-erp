from fastapi import WebSocket, Depends
from starlette.websockets import WebSocketDisconnect
import asyncio
from broadcaster import Broadcast
from fastapi import APIRouter
from notification.notification_crud import receive_message, echo_message
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/api')

broadcast = Broadcast("redis://localhost:6379")


@router.on_event("startup")
async def startup():
    await broadcast.connect()


@router.on_event("shutdown")
async def shutdown():
    await broadcast.disconnect()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str, channel: str, db: Session = Depends(get_db)):
    await websocket.accept()

    try:
        while True:
            receive_message_task = asyncio.create_task(
                receive_message(websocket, username=username, channel=channel))
            echo_message_task = asyncio.create_task(
                echo_message(db=db, websocket=websocket, username=username))
            done, pending = await asyncio.wait(
                {echo_message_task, receive_message_task}, return_when=asyncio.FIRST_COMPLETED)

            [task.cancel() for task in pending]
            [task.result() for task in done]

    except WebSocketDisconnect:
        await websocket.close()
