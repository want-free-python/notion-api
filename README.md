# notion-api

### meaning
1. api.py
: api 역할을 하는 함수들의 파일
2. mocking.py
: 해당 파일을 실행하면 mock data(가짜 데이터)를 db에 넣어줌
3. models.py
: sqlalchemy를 사용해서 모델 생성

### Setup guide
1. `python models.py` 명령어를 실행하여 : sqlite3 데이터베이스에 테이블을 생성한다.
2. `python mocking.py` 명령어를 실행하여 : 생성된 테이블에 mock data를 넣어준다.
3. `python api.py` 명령어를 실행하여 : response값으로 기대하는 return값이 나오는지 확인한다.