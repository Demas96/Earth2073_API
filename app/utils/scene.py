from app.models.models import scenes_table, windows_table
from app.db import database


async def create_scene(scene):
    query = scenes_table.insert().values(
        name=scene.name,
        path_img=scene.path_img
    )
    scene_id = await database.execute(query)
    return {'scene_id': scene_id, 'name': scene.name}


async def create_window(window):
    query = windows_table.insert().values(
        scene_id=window.scene_id,
        serial_number=window.serial_number,
        text=window.text,
        character=window.character,
        version=window.version,
        path_img=window.path_img
    )
    window_id = await database.execute(query)
    return {'window_id': window_id}


async def get_scene(name):
    query = scenes_table.select().where(scenes_table.c.name == name)
    scene = await database.fetch_all(query)
    query = windows_table.select().where(windows_table.c.scene_id == scene[0]['id'])
    windows = await database.fetch_all(query)
    return {'scene': scene, 'windows': windows}
