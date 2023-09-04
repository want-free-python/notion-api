from os import getenv
from typing import Tuple, Union, Optional, List

import mysql.connector
from dotenv import load_dotenv

load_dotenv(verbose=True)

DB_CONFIG = {
    "host": getenv('DB_HOST'),
    "user": getenv('DB_USER'),
    "password": getenv('DB_PASSWORD'),
    "database": getenv('DB_NAME'),
}

def connect_to_mysql() -> Tuple[
    Optional[
        mysql.connector.connection.MySQLConnection
    ], 
    Optional[
        mysql.connector.cursor.MySQLCursor]
    ]:
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor

    except mysql.connector.Error as e:
        print(f"MySQL 오류 발생: {e}")
    
    return None, None

def close_mysql_connection(
    connection: Optional[
        mysql.connector.connection.MySQLConnection
    ], 
    cursor: Optional[
        mysql.connector.cursor.MySQLCursor
    ]) -> None:
    if connection:
        connection.close()


def execute_sql_query(
    sql_query: str, 
    fetchall: bool = False
    ) -> Union[None, List[Tuple]]:
    connection, cursor = connect_to_mysql()

    if not connection:
        return None

    try:
        cursor.execute(sql_query)
        connection.commit()

        if fetchall:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()

        return result

    except mysql.connector.Error as e:
        print(f"MySQL 오류 발생: {e}")
        return None

    finally:
        close_mysql_connection(connection, cursor)
