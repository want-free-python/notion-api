from models import conn, cursor


class Page:
    def __init__(self, id: int, title: str, content: str, parent_id: int | None = None):
        self.title = title
        self.content = content
        self.parent_id = parent_id
        self.id = None

    def save(self):
        # 데이터베이스에 페이지 추가
        cursor.execute('''
            INSERT INTO pages (title, content, parent_id)
            VALUES (?, ?, ?)
        ''', (self.title, self.content, self.parent_id))
        conn.commit()
        self.id = cursor.lastrowid

    @staticmethod
    def get_children(parent_id):
        # 부모 페이지의 자식 페이지 조회
        cursor.execute('SELECT * FROM pages WHERE parent_id = ?', (parent_id,))
        rows = cursor.fetchall()
        children = []
        for row in rows:
            page = Page(row[1], row[2], row[3])
            page.id = row[0]
            children.append(page)
        return children

all_pages = []

# 페이지 생성 및 저장 예제
parent_page = Page(1, "Parent Page", "This is the parent page content")
parent_page.save()

child_page1 = Page(2, "Child Page 1", "This is child page 1 content", parent_id=parent_page.id)
child_page1.save()

child_page2 = Page(3, "Child Page 2", "This is child page 2 content", parent_id=parent_page.id)
child_page2.save()

all_pages.extend([parent_page, child_page1, child_page2])

print(all_pages)


# # 페이지 데이터 생성
# pages = [
#     Page(1, "페이지 1", "이것은 페이지 1의 내용입니다."),
#     Page(2, "페이지 2", "이것은 페이지 2의 내용입니다."),
#     Page(3, "페이지 3", "이것은 페이지 3의 내용입니다.", parent_id=1),  # 페이지 1의 하위 페이지
#     Page(4, "페이지 4", "이것은 페이지 4의 내용입니다.", parent_id=2),  # 페이지 2의 하위 페이지
# ]