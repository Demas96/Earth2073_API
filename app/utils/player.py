from app.models.models import players_table
from app.db import database


async def get_player_by_id(id: int):
    query = players_table.select().where(players_table.c.id == id)
    return await database.fetch_one(query)


async def create_player(name: str):
    query = players_table.insert().values(
        name=name
    )
    user_id = await database.execute(query)

    return {"id": user_id}

async def update_player_level(id: int, level: int):
    query = players_table.update().where(players_table.c.id == id).values(level=level)
    await database.execute(query)

    return 'Ok'

async def update_player_time(id: int, time: str):
    query = players_table.update().where(players_table.c.id == id).values(time=time)
    await database.execute(query)
    return 'Ok'
