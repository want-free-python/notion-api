import json

from db import get_connection
from models import Page, Breadcrumbs


def insert_page(title: str, content: str, parent_id: int | None = None) -> int:
    connection = get_connection()
    cur = connection.cursor()
    sql = "insert into page(title, content, parent_id) values(%s, %s, %s)"
    cur.execute(sql, (title, content, parent_id))
    page_id = cur.lastrowid
    connection.commit()
    connection.close()

    return page_id


def update_page(page_id: int, title: str, content: str, parent_id: int | None = None) -> None:
    connection = get_connection()
    cur = connection.cursor()
    sql = "update page set title=%s, content=%s, parent_id=%s where id=%s"
    cur.execute(sql, (title, content, parent_id, page_id))
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


def select_breadcrumbs_by_page_id(page_id: int) -> Breadcrumbs:
    connection = get_connection()
    cur = connection.cursor()
    sql = "select * from breadcrumbs where page_id=%s"
    cur.execute(sql, page_id)
    result = cur.fetchone()
    connection.close()
    if not result:
        return None
    return Breadcrumbs(*result)


def insert_breadcrumbs(page_id: int, breadcrumbs: dict) -> None:
    connection = get_connection()
    cur = connection.cursor()
    sql = "insert into breadcrumbs(page_id, breadcrumbs) values(%s, %s)"
    cur.execute(sql, (page_id, json.dumps(breadcrumbs)))
    connection.commit()
    connection.close()


def update_breadcrumbs(page_id: int, breadcrumbs: dict) -> None:
    connection = get_connection()
    cur = connection.cursor()
    sql = "update breadcrumbs set breadcrumbs=%s where page_id=%s"
    cur.execute(sql, (json.dumps(breadcrumbs), page_id))
    connection.commit()
    connection.close()
