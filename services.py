from collections import deque

from crud import (
    select_pages_by_parent_id,
    select_page,
    insert_page,
    select_breadcrumbs_by_page_id,
    insert_breadcrumbs, update_page, update_breadcrumbs,
)
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
    breadcrumbs = select_breadcrumbs_by_page_id(page_id)
    if not breadcrumbs:
        return []

    return [
        PageSummarySchema(bc["page_id"], bc["title"])
        for bc in breadcrumbs.breadcrumbs["order"]
    ]


# @TODO 트랜잭션 필요
def create_page(title: str, content: str, parent_id: int | None = None) -> None:
    page_id = insert_page(title, content, parent_id)
    breadcrumbs = dict()
    breadcrumbs["order"] = []
    if parent_id:
        parent_breadcrumbs = select_breadcrumbs_by_page_id(parent_id)
        breadcrumbs["order"].extend(parent_breadcrumbs.breadcrumbs["order"])

    breadcrumbs["order"].append({"title": title, "page_id": page_id})
    insert_breadcrumbs(page_id, breadcrumbs)



# @TODO 트랜잭션 필요
def rearrange_breadcrumbs(page_id: int) -> None:
    q = deque([page_id])
    while q:
        page_id = q.popleft()
        sub_page_ids = [sub_page.id for sub_page in select_pages_by_parent_id(page_id)]
        q.extend(sub_page_ids)

        page = select_page(page_id)
        breadcrumbs = dict()
        breadcrumbs["order"] = []
        if page and page.parent_id:
            parent_breadcrumbs = select_breadcrumbs_by_page_id(page.parent_id)
            breadcrumbs["order"].extend(parent_breadcrumbs.breadcrumbs["order"])

        breadcrumbs["order"].append({"title": page.title, "page_id": page_id})
        update_breadcrumbs(page_id, breadcrumbs)


# @TODO 트랜잭션 필요
def modify_page(page_id: int, title: str, content: str, parent_id: int | None = None) -> None:
    update_page(page_id, title, content, parent_id)
    rearrange_breadcrumbs(page_id)
