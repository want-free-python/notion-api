# notion-api


### settings
sqlalchemy 를 사용하기 위해 가상환경을 생성하고 sqlalchemy를 다운 받는다.
1. python -m venv notion
2. source notion/bin/activate
3. pip install sqlalchemy


### meaning
1. api.py
: api 역할을 하는 함수들의 파일
2. mocking.py
: 해당 파일을 실행하면 mock data(가짜 데이터)를 db에 넣어줌
3. models.py
: sqlalchemy를 사용해서 모델 생성