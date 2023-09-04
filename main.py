from pprint import pprint


from schemas import PageResponseSchema
from services import get_sub_pages, get_breadcrumbs, get_page
from settings import initialize_dummy_data, modify_parent_page_id

initialize_dummy_data()
modify_parent_page_id()

while True:
    page_id = int(input("페이지 ID: "))
    page = get_page(page_id)
    if not page:
        print("Error 404")
        break

    pprint(
        PageResponseSchema(
            page.id,
            page.title,
            page.content,
            get_sub_pages(page_id),
            get_breadcrumbs(page_id),
        ).to_dict()
    )
