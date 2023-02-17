from fastapi import WebSocket, Depends, WebSocketDisconnect
import asyncio
from broadcaster import Broadcast
from fastapi import APIRouter
from notification.notification_crud import receive_message, echo_message, userInfo, manager
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
    await manager.connect(websocket=websocket, username=username)
    try:
        while True:
            manager.active_connections[websocket]
            receive_message_task = asyncio.create_task(
                receive_message(websocket, username=username, channel=channel))
            echo_message_task = asyncio.create_task(
                echo_message(db=db, websocket=websocket, username=username))
            userinfo_task = asyncio.create_task(
                userInfo(websocket=websocket))
            done, pending = await asyncio.wait(
                {echo_message_task, receive_message_task, userinfo_task}, return_when=asyncio.FIRST_COMPLETED)

            [task.cancel() for task in pending]
            [task.result() for task in done]

    except WebSocketDisconnect:
        manager.disconnect(websocket=websocket, username=username)
        print("Client disconnected")
    except KeyError:
        print(f"{username} Account Disconnected")
""" 

@router.websocket("/usercount")
async def usercount(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            Usercount_task = asyncio.create_task(
                userinfo(websocket=websocket))
            done, pending = await asyncio.wait(
                {Usercount_task}, return_when=asyncio.ALL_COMPLETED)
            for task in pending:
                task.cancel()
            for task in done:
                task.result()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected2")
 """
