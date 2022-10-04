import datetime
from typing import Union

from fastapi import FastAPI, Request, WebSocket, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.websockets import WebSocketDisconnect

from exceptions.ResponseException import ResponseException
from models import Auth, Message
from routes import auth, news, message
from routes import users
from routes import transfer
from routes import change
from routes import history, test
from utils.dependencies import get_auth_argument, get_db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix='/auth')
app.include_router(users.router, prefix='/users')
app.include_router(transfer.router, prefix='/transfer')
app.include_router(change.router, prefix='/change')
app.include_router(history.router, prefix='/history')
app.include_router(news.router, prefix='/news')
app.include_router(message.router, prefix='/message')
app.include_router(test.router, prefix='')


@app.exception_handler(ResponseException)
def exception_handler(req: Request, exc: ResponseException):
    return exc.get_response()


class ConnectionManager:
    connections: list[dict] = []

    def connect(self, ws):
        self.connections.append(ws)

    def disconnect(self, ws):
        self.connections.remove(ws)

    async def broadcast(self, text):
        for i in self.connections:
            await i['ws'].send_json(text)


connection_manager = ConnectionManager()


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket, auth: Union[Auth, None] = Depends(get_auth_argument), db: Session=Depends(get_db)):
    if auth is None:
        raise ResponseException(text='dont your user', status=400)
    await websocket.accept()
    connection_manager.connect({
        'ws': websocket,
        'auth': auth
    })
    await connection_manager.broadcast({
        'user': auth.email,
        'type': 'online'
    })
    try:
        while True:
            data = await websocket.receive_text()
            await connection_manager.broadcast({
                'type': 'message',
                'user': auth.email,
                'text': data
            })

            message = Message(sender_id=auth.id, text=data, date=datetime.datetime.now())
            db.add(message)
            db.commit()

    except WebSocketDisconnect:
        connection_manager.disconnect({
            'ws': websocket,
            'auth': auth
        })
        await connection_manager.broadcast({
            'user': auth.email,
            'type': 'offline'
        })


# сообщенияны базага жазуу историяны кайра чыгаруу
