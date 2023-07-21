import sqlalchemy


metadata = sqlalchemy.MetaData()


players_table = sqlalchemy.Table(
    "players",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("level", sqlalchemy.Integer, default=0),
    sqlalchemy.Column("time", sqlalchemy.String(100), default='0'),
)

scenes_table = sqlalchemy.Table(
    "scenes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("path_img", sqlalchemy.String),
)

windows_table = sqlalchemy.Table(
    "windows",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("scene_id", sqlalchemy.ForeignKey("scenes.id")),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("character", sqlalchemy.String(100)),
    sqlalchemy.Column("path_img", sqlalchemy.String),
)