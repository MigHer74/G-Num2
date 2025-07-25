from pathlib import Path
import src.db_tools as db


def verify_database():
    dbFolder = "db"
    dbFile = "gnum2.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir("db")

    if not Path(dbFile).is_file():
        db.create_table()
