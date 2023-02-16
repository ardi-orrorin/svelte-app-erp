from fastapi import WebSocket, Depends, WebSocketDisconnect

import asyncio
from broadcaster import Broadcast
from fastapi import APIRouter
from notification.notification_crud import receive_message, echo_message
from database import get_db
from sqlalchemy.orm import Session
import json
from typing import List
import time


router = APIRouter(prefix='/api')

broadcast = Broadcast("redis://localhost:6379")


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    def usercount(self) -> int:
        return len(self.active_connections)


manager = ConnectionManager()


@router.on_event("startup")
async def startup():
    await broadcast.connect()


@router.on_event("shutdown")
async def shutdown():
    await broadcast.disconnect()


async def userinfo(websocket: WebSocket):
    await asyncio.sleep(1)
    count = manager.usercount()
    test = {"count": count}
    test = json.dumps(test)
    await websocket.send_text(test)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, username: str, channel: str, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            receive_message_task = asyncio.create_task(
                receive_message(websocket, username=username, channel=channel))
            echo_message_task = asyncio.create_task(
                echo_message(db=db, websocket=websocket, username=username))
            userinfo_task = asyncio.create_task(userinfo(websocket=websocket))
            done, pending = await asyncio.wait(
                {echo_message_task, receive_message_task, userinfo_task}, return_when=asyncio.FIRST_COMPLETED)

            [task.cancel() for task in pending]
            [task.result() for task in done]

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected1")
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
