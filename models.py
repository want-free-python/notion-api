import json


class Page:
    def __init__(self, id: int, title: str, content: str, parent_id: int | None = None):
        self.id = id
        self.title = title
        self.content = content
        self.parent_id = parent_id


class Breadcrumbs:
    def __init__(self, id: int, page_id: int, breadcrumbs: str):
        self.id = id
        self.page_id = page_id
        self.breadcrumbs = json.loads(breadcrumbs)
