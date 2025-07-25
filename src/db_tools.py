import sqlite3


def connect_db():
    db_connection = sqlite3.connect("db/gnum2.db")
    return db_connection


def create_table():
    dbcon = connect_db()
    dbcur = dbcon.cursor()

    sqlrow = """CREATE TABLE IF NOT EXISTS 'games' (
    game_type TEXT,
    game_week TEXT,
    game_number INTEGER,
    number_1 INTEGER,
    number_2 INTEGER,
    number_3 INTEGER,
    number_4 INTEGER,
    number_5 INTEGER,
    number_6 INTEGER
    );"""

    dbcur.execute(sqlrow)
    dbcon.commit()
    dbcon.close()
