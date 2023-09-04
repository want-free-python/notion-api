from typing import List

from db_settings import execute_sql_query
from models import Page

def get_page(page_id: int) -> Page:
    result = execute_sql_query(
        sql_query=f"""
        SELECT id, title, parent_id 
        FROM page
        WHERE id = {page_id};
        """,
        fetchall=False
    )
    page = Page(*result)
    return page

def get_sub_pages(page_id: int) -> List[int]:
    sub_pages = execute_sql_query(
        sql_query=f"""
        SELECT id
        FROM page
        WHERE parent_id = {page_id};
        """,
        fetchall=True
    )
    sub_pages = [page[0] for page in sub_pages]
    return sub_pages

def get_breadcrumbs(sub_page: List[int]) -> List[str]:
    pass
    
    

