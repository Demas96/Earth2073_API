import sqlalchemy

from fastapi import FastAPI

from app.db import DATABASE_URL, database


app = FastAPI()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
