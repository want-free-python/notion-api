from pprint import pprint



##########      DB      ##########
pages = {}


##########      Model      ##########
class Page:
    def __init__(
        self, pk: int, title: str = None, content: str = None, sub_pages: list = []
    ):
        self.pk = pk
        self.title = title
        self.content = content
        self.sub_pages = sub_pages  # self ref

    # 단순 데이터 출력용 함수입니다.
    def get_data(self):
        return {
            "pk": self.pk,
            "title": self.title,
            "content": self.content,
            "sub_pages": self.sub_pages,
        }


##########      API      ##########


def get_page(breadcrumb: list, page_pk: int) -> dict:
    """요청받은 페이지 정보 api

    Args:
        breadcrumb (list): 이전 페이지의 breadcrumb
        page_pk (int): 요청받은 페이지의 pk값

    Returns:
        dict: 페이지 정보
    """

    def get_breadcrumb(breadcrumb: list, page_pk: int) -> list:
        """요청받은 페이지에서 breadcrumb 리스트의 상태 반환 함수
        Args:
            breadcrumb (list): 이전 페이지의 breadcrumb
            page_pk (int): 요청받은 페이지의 pk값

        Returns:
            list: 요청받은 페이지에서의 breadcrumb
        """

        # 요청받은 페이지가 이전 breadcrumb 내에 있다면 breadcrumb 내의 pk값 반환
        if page_pk in breadcrumb:
            return breadcrumb[: breadcrumb.index(page_pk) + 1]

        # breadcrumb가 비어있지 않고 하위 페이지라면 pk값 추가
        elif breadcrumb and page_pk in pages[breadcrumb[-1]].sub_pages:
            breadcrumb.append(page_pk)
            return breadcrumb

        # 페이지를 타지않고 곧바로 들어왔다면 해당 pk값에서 시작
        else:
            return [page_pk]

    # 페이지 데이터에서 breadcrumb데이터를 추가하여 반환
    data = pages[page_pk].get_data()
    data["breadcrumb"] = get_breadcrumb(breadcrumb=breadcrumb, page_pk=page_pk)
    return data


##########      settings      ##########
for i in range(10):
    pages[i] = Page(pk=i, title=f"title {i}", content=f"content {i}")

pages[0].sub_pages = [1, 2, 3]
pages[1].sub_pages = [4, 5, 6]
pages[4].sub_pages = [7, 8, 9]


##########      requests      ##########
page_pk = 0
breadcrumb = []
while True:
    print("\n\n\n")
    print("현재 페이지 정보")
    data = get_page(breadcrumb=breadcrumb, page_pk=page_pk)
    pprint(data)
    breadcrumb = data["breadcrumb"]
    print("-" * 20)
    page_pk = int(input("다음 페이지 번호 : "))
