from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from exceptions.ResponseException import ResponseException
from routes import auth, news
from routes import users
from routes import transfer
from routes import change
from routes import history, test

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
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
app.include_router(test.router, prefix='')


@app.exception_handler(ResponseException)
def exception_handler(req: Request, exc: ResponseException):
    return exc.get_response()
