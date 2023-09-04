from db import get_connection
from services import create_page, modify_page


def create_table() -> None:
    connection = get_connection()
    cur = connection.cursor()
    sql = f"\
        CREATE TABLE page(\
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        title varchar(256) NOT NULL,\
        content text NOT NULL,\
        parent_id int,\
        FOREIGN KEY (parent_id) REFERENCES page(id)\
        );"
    cur.execute(sql)
    sql = f"\
        CREATE TABLE breadcrumbs(\
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        page_id int,\
        breadcrumbs text NOT NULL,\
        FOREIGN KEY (page_id) REFERENCES page(id)\
        );"
    cur.execute(sql)
    connection.commit()
    connection.close()


def drop_table() -> None:
    connection = get_connection()
    cur = connection.cursor()
    sql = "SHOW TABLES LIKE 'breadcrumbs';"
    cur.execute(sql)
    if cur.fetchone():
        sql = "DROP TABLE breadcrumbs;"
        cur.execute(sql)
    sql = "SHOW TABLES LIKE 'page';"
    cur.execute(sql)
    if cur.fetchone():
        sql = "DROP TABLE page;"
        cur.execute(sql)
    connection.commit()
    connection.close()


def initialize_dummy_data() -> None:
    drop_table()
    create_table()
    create_page("page 1", "content")
    create_page("page 2", "content", 1)
    create_page("page 3", "content", 1)
    create_page("page 4", "content", 2)
    create_page("page 5", "content", 3)
    create_page("page 6", "content", 1)
    create_page("page 7", "content")
    create_page("page 8", "content", 3)
    create_page("page 9", "content", 4)
    create_page("page 10", "content", 9)


def modify_parent_page_id() -> None:
    modify_page(1, "page 1", "content", 7)
