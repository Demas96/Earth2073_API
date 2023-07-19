import sqlalchemy

from fastapi import FastAPI

from app.db import DATABASE_URL, database
from app.utils.player import get_player_by_id, create_player, update_player_level, update_player_time


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


@app.get("/player")
async def get_player(id: int):
    return await get_player_by_id(id)


@app.post("/player")
async def create(name: str):
    return await create_player(name=name)


@app.put("/player_level")
async def update_level(id: int, level: int):
    return await update_player_level(id, level)

@app.put("/player_time")
async def update_time(id: int, time: str):
    return await update_player_time(id, time)