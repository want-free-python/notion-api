import pymysql
from pymysql import Connection

from env import HOST, PORT, USER, PASSWORD, DB


def get_connection() -> Connection:
    return pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        db=DB,
        charset="utf8",
    )
