import sqlalchemy

from fastapi import FastAPI
from pydantic import BaseModel

from app.db import DATABASE_URL, database
from app.utils.player import get_player_by_id, create_player, update_player_level, update_player_time
from app.utils.scene import create_scene, create_window, get_scene

app = FastAPI()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


class PlayerValid(BaseModel):
    name: str


class ScenesValid(BaseModel):
    name: str
    path_img: str


class WindowsValid(BaseModel):
    scene_id: int
    text: str
    character: str
    path_img: str


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
async def create(name: PlayerValid):
    return await create_player(name=name)


@app.put("/player_level")
async def update_level(id: int, level: int):
    return await update_player_level(id, level)


@app.put("/player_time")
async def update_time(id: int, time: str):
    return await update_player_time(id, time)


@app.post("/scenes")
async def add_scene(scene: ScenesValid):
    return await create_scene(scene)


@app.post("/windows")
async def add_window(window: WindowsValid):
    return await create_window(window)


@app.get("/scenes/")
async def scene(name: str):
    return await get_scene(name)
