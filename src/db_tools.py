import sqlite3


def connect_db():
    db_connection = sqlite3.connect("db/gnum2.db")
    return db_connection
