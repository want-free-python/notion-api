from db import get_connection
from models import Page


def insert_page(title: str, content: str, parent_id: int | None = None):
    connection = get_connection()
    cur = connection.cursor()
    sql = "insert into page(title, content, parent_id) values(%s, %s, %s)"
    cur.execute(sql, (title, content, parent_id))
    connection.commit()
    connection.close()


def select_page(page_id: int) -> Page | None:
    connection = get_connection()
    cur = connection.cursor()
    sql = "select * from page where id=%s"
    cur.execute(sql, page_id)
    result = cur.fetchone()
    connection.close()
    if not result:
        return None
    return Page(*result)


def select_pages_by_parent_id(parent_page_id: int) -> list[Page]:
    connection = get_connection()
    cur = connection.cursor()
    sql = "select * from page where parent_id=%s"
    cur.execute(sql, parent_page_id)
    results = cur.fetchall()
    connection.close()
    if not results:
        return []
    return [Page(*res) for res in results]
