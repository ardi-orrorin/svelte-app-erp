from fastapi import WebSocket, Depends
from notification import notification_router
from notification.notification_schema import Notification
from models import User, Notification as modelNotification
import json
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime
from sqlalchemy import func


async def receive_message(websocket: WebSocket, username: str, channel: str):
    async with notification_router.broadcast.subscribe(channel=channel) as subscriber:

        async for event in subscriber:
            message_event = Notification.parse_raw(event.message)
            if message_event.username == username:
                await websocket.send_text("".join(message_event.json()))


async def echo_message(db: Session, websocket: WebSocket, username: str):

    data = await websocket.receive_text()
    data = json.loads(data)

    event = Notification(
        message=data['message'], username=username, channel=data["channel"], create_date=data['create_date'])

    await notification_router.broadcast.publish(channel=data['channel'], message=event.json())

    notifiCation(db=db, data=data, username=username)


def notifiCation(db: Session, data: Notification, username: str):

    message, channel, create_date = data.values()
    user_id = db.query(User.id).filter(User.user_id == username).first()[0]
    last_id = db.query(func.max(modelNotification.id).label("id")).all()[0][0]
    if last_id == None:
        last_id = 0

    db_notification = modelNotification(id=last_id+1,
                                        channel=channel, user_id=user_id, message=message, create_date=create_date, authority=1)
    db.add(db_notification)
    db.commit()
