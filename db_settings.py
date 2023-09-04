import mysql.connector
from dotenv import load_dotenv
import os 

load_dotenv()

env = os.environ.get('env')

DB_CONFIG = {
    "host": env('DB_HOST'),
    "user": env('DB_USER'),
    "password": env('DB_PASSWORD'),
    "database": env('DB_NAME'),
}

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            cursor = connection.cursor()

        return connection, cursor

    except mysql.connector.Error as e:
        print(f"MySQL 오류 발생: {e}")
        return None, None

def close_mysql_connection(connection, cursor):
    if connection:
        connection.close()


def execute_sql_query(sql_query, fetchall=False):
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
