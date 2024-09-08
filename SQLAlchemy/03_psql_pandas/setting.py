from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# 接続先DBの設定
# DATABASE = "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type}"

#DATABASE = 'sqlite:///db.sqlite3'
DATABASE = "postgresql://postgres:postgres@localhost:5432/testdb2"


# Engine の作成
Engine = create_engine(
  DATABASE,
  #encoding="utf-8",
  echo=False
)
Base = declarative_base()

### Sessionの作成
##session = Session(
##  autocommit = False,
##  autoflush = True,
##  bind = Engine
##)

from sqlalchemy.orm import scoped_session, sessionmaker

# Sessionの作成
session = scoped_session(
    sessionmaker(
        autocommit = False,
	autoflush = False,
	bind = Engine
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
