from pathlib import Path
import src.db_tools as db


def verify_database():
    dbFolder = "D:/DBA/SQLite/G-Num2/"
    dbFile = "gnum2.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir(dbFolder)

    if not Path(dbFolder + dbFile).is_file():
        db.create_table()
        db.load_initial_values()
