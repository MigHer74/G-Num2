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


def get_latest_data():
    sqlrow1 = "SELECT * FROM games WHERE game_type = 'S' AND game_week = 'W1';"
    sqlrow2 = """SELECT * FROM games WHERE game_type = 'L' AND game_week = 'W1'
    ORDER BY game_number;"""

    dbcon = connect_db()
    dbcur = dbcon.cursor()
    data_short = dbcur.execute(sqlrow1).fetchone()
    data_long = dbcur.execute(sqlrow2).fetchall()
    dbcon.close()

    return data_short, data_long
