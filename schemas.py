class PageSchema:
    def __init__(self, id: int, title: str, content: str, parent_id: int | None = None):
        self.id = id
        self.title = title
        self.content = content
        self.parent_id = parent_id


class PageSummarySchema:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title


class PageResponseSchema:
    def __init__(
        self,
        id: int,
        title: str,
        content: str,
        sub_pages: list[PageSummarySchema],
        breadcrumbs: list[PageSummarySchema],
    ):
        self.id = id
        self.title = title
        self.content = content
        self.sub_pages = sub_pages
        self.breadcrumbs = breadcrumbs

    def to_dict(self):
        dic = self.__dict__
        dic["sub_pages"] = [sub_page.__dict__ for sub_page in self.sub_pages]
        dic["breadcrumbs"] = [breadcrumb.__dict__ for breadcrumb in self.breadcrumbs]

        return dic
