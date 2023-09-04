from collections import deque
from typing import Deque

from crud import select_pages_by_parent_id, select_page
from schemas import PageSummarySchema, PageSchema


def get_page(page_id: int) -> PageSchema | None:
    page = select_page(page_id)
    if not page:
        return None
    return PageSchema(page.id, page.title, page.content, page.parent_id)


def get_sub_pages(page_id: int) -> list[PageSummarySchema]:
    return [
        PageSummarySchema(sub_page.id, sub_page.title)
        for sub_page in select_pages_by_parent_id(page_id)
    ]


def get_breadcrumbs(page_id: int) -> list[PageSummarySchema]:
    page = select_page(page_id)
    if not page:
        return []

    breadcrumbs: Deque[PageSummarySchema] = deque(
        [PageSummarySchema(page.id, page.title)]
    )
    while page and page.parent_id:
        page = select_page(page.parent_id)
        breadcrumbs.appendleft(PageSummarySchema(page.id, page.title))

    return list(breadcrumbs)
