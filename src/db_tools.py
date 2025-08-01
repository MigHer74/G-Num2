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


def load_initial_values():
    dbcon = connect_db()
    dbcur = dbcon.cursor()

    for game in range(1, 7):
        sqlrow = f"INSERT INTO games\
            VALUES('S', 'W{game}', {game}, 0, 0, 0, 0, 0, 0);"
        dbcur.execute(sqlrow)

    for week in range(1, 7):
        for game in range(1, 4):
            sqlrow = f"INSERT INTO games\
                VALUES('L', 'W{week}', {game}, 0, 0, 0, 0, 0, 0);"
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


def update_games(game_type):
    dblist = ["W6", "W5", "W4", "W3", "W2", "W1"]

    if game_type == "short":
        dbtype = "S"
    else:
        dbtype = "L"

    dbcon = connect_db()
    dbcur = dbcon.cursor()

    row1 = "DELETE FROM games WHERE gWeek ='W6'AND gType = '{dbtype}';"
    row2 = f"AND gType = '{dbtype}';"
    command = row1 + row2
    dbcur.execute(command)

    for dbindex in range(1, 6):
        row1 = f"UPDATE games SET gWeek = '{dblist[dbindex-1]}'"
        row2 = f"WHERE gWeek = '{dblist[dbindex]}' AND gType = '{dbtype}';"
        command = row1 + row2
        dbcur.execute(command)

    dbcon.commit()
    dbcon.close()