class Page:
    def __init__(self, id: int, title: str, content: str, parent_id: int | None = None):
        self.id = id
        self.title = title
        self.content = content
        self.parent_id = parent_id
