from sqlalchemy import Column, Integer, String, Float, DateTime

from setting import Engine
from setting import Base


class User(Base):
    """
    ユーザモデル
    """

    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))
    created = Column('created', DateTime)
    updated = Column('updated', DateTime)

if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)


