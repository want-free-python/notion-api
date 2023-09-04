class Page:
    def __init__(self, id: int, title: str, parent_id: int):
        self.id = id
        self.title = title
        self.parent_id = parent_id