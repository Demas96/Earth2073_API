import databases

from app.config import HOST_DB, PORT_DB, USER_DB, NAME_DB, PASSWORD_DB


DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"
database = databases.Database(DATABASE_URL)