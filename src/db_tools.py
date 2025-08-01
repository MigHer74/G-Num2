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
            VALUES('S', 'W{game}', 1, 0, 0, 0, 0, 0, 0);"
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
    week_list = ["W6", "W5", "W4", "W3", "W2", "W1"]

    if game_type == "short":
        game_type = "S"
    else:
        game_type = "L"

    dbcon = connect_db()
    dbcur = dbcon.cursor()

    sqlrow = f"DELETE FROM games WHERE game_week ='W6'AND \
        game_type = '{game_type}';"

    dbcur.execute(sqlrow)

    for dbindex in range(1, 6):
        sqlrow = f"UPDATE games SET game_week = '{week_list[dbindex-1]}' \
            WHERE game_week = '{week_list[dbindex]}' \
            AND game_type = '{game_type}';"
        dbcur.execute(sqlrow)

    dbcon.commit()
    dbcon.close()


def insert_values(data):
    dbcon = connect_db()
    dbcur = dbcon.cursor()
    dbcur.execute("INSERT INTO games VALUES(?,?,?,?,?,?,?,?,?)", (data))
    dbcon.commit()
    dbcon.close()
