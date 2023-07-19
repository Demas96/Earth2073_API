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