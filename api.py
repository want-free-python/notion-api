from mocking import all_pages, Page
from models import conn, cursor
import json

# 페이지 정보를 JSON 형식으로 반환하는 함수
def get_page_info(page, all_pages):
    page_info = {
        "id": page.id,
        "title": page.title,
        "content": page.content,
    }
    # 하위 페이지 정보 수집
    subpages = [get_page_info(subpage, all_pages) for subpage in all_pages if subpage.parent_id == page.id]
    if subpages:
        page_info["subpages"] = subpages
    return page_info

# 모든 페이지 정보를 가져오기
all_page_info = [get_page_info(page, all_pages) for page in all_pages]

# 결과 출력
print(json.dumps(all_page_info, indent=2, ensure_ascii=False))  # indent를 사용해서 가독성있는 return값 반환


# # 페이지 정보를 가져오는 함수
# def get_page_info(page_id):
#     cursor.execute("SELECT id, title, content, parent_id FROM pages WHERE id = ?", (page_id,))
#     row = cursor.fetchone()
#     if row:
#         page_id, title, content, parent_id = row
#         page = Page(page_id, title, content, parent_id)
#         return page
#     else:
#         return None

# # 모든 페이지 정보를 가져오기
# def get_all_pages():
#     cursor.execute("SELECT id FROM pages")
#     page_ids = [row[0] for row in cursor.fetchall()]
#     pages = [get_page_info(page_id) for page_id in page_ids]
#     return pages

# # 모든 페이지 정보 가져오기
# all_pages = get_all_pages()

# # 결과 출력
# all_page_info = [get_page_info(page.id).__dict__ for page in all_pages]  # Page 객체를 dictionary로 변환
# print(json.dumps(all_page_info, indent=2, ensure_ascii=False))



# # 브레드크럼스 함수


# import sqlite3
# from models import conn, cursor

# def get_breadcrumbs(page_id):

#     breadcrumbs = []
#     while page_id is not None:
#         cursor.execute('SELECT title, parent_id FROM pages WHERE id = ?', (page_id,))
#         result = cursor.fetchone()
#         if result:
#             title, parent_id = result
#             breadcrumbs.insert(0, title)  # 가장 최상위 페이지의 타이틀을 앞에 추가
#             page_id = parent_id
#         else:
#             page_id = None

#     conn.close()
#     return '/'.join(breadcrumbs)

# # 페이지 ID를 지정하여 브레드크럼스를 가져옵니다.
# page_id = 4  # 예제로 페이지 ID를 4로 설정
# breadcrumbs = get_breadcrumbs(page_id)
# print(breadcrumbs)  # 예를 들어, "Home/Category/Subcategory/Product"와 같은 출력이 될 것입니다.