from dotenv import load_dotenv
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Text, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
import os

Base = declarative_base()


class Settings:
    def __init__(self) -> None:
        self.set_env()
        self._engine = self.connect_database()

    def set_env(self):
        env = os.getenv("ENV", "test")
        env_file = f".env.{env}"
        load_dotenv(env_file)

    def connect_database(self):
        user = os.getenv("MY_SQL_USER")
        password = os.getenv("MY_SQL_PASSWORD")
        database = os.getenv("MY_SQL_DATABASE")
        port = os.getenv("MY_SQL_PORT")
        host = os.getenv("MY_SQL_HOST", "localhost")
        string_url = (
            f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
        )
        engine = create_engine(string_url, echo=True)

        return engine


class Page(Base):

    __tablename__ = "page"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(Text)
    parent_id = Column(
        Integer, ForeignKey("page.id", ondelete="CASCADE"), nullable=True
    )
    children = relationship("Page", back_populates="parent")
    parent = relationship("Page", back_populates="children", remote_side=[id])


class PageSerializer:

    db_table = Page
    fields = ("id", "title", "content", "parent_id")

    def __init__(self) -> None:
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        engine = instance.engine
        with engine.begin() as connection:
            raw_query = f"""SHOW COLUMNS FROM {self.db_table.__tablename__};"""
            result = connection.execute(text(raw_query))
            fields = [output[0] for output in result]
            validated_fields = self.field_validation(fields)

        return validated_fields

    def field_validation(self, fields):
        for field in self.fields:
            if field not in fields:
                raise ValueError(f"No matching {field} in {self.db_table} table.")
        return fields

    def get_data(self, row):
        for field1, field2 in zip(self.fields, row):
            self.data[field1] = field2
        return self.data


class PageRetrieveAPI:

    db_table = Page
    serializer = PageSerializer()

    def __init__(self) -> None:
        self._settings = Settings()
        self.create_table()

    @property
    def engine(self):
        return self._settings._engine

    def create_table(self):
        engine = self.engine
        with engine.begin() as connection:
            if not engine.dialect.has_table(
                connection=connection, table_name=self.db_table.__tablename__
            ):
                Base.metadata.create_all(engine)
                connection.close()
        return

    def retrieve(self, id: int):
        engine = self.engine
        with engine.begin() as connection:
            raw_query = (
                f"""SELECT * FROM {self.db_table.__tablename__} WHERE id = {id};"""
            )
            result = connection.execute(text(raw_query))

        row = result.first()
        data = self.serializer.get_data(row)

        return data

    # dummy data 생성용
    def insert(self):
        engine = self.engine
        with engine.begin() as connection:
            result = connection.execute(
                insert(table=self.db_table),
                [
                    {"title": "title1", "content": "content1"},
                    {"title": "title2", "content": "content2"},
                    {"title": "title3", "content": "content3", "parent_id": 2},
                ],
            )

        return result
