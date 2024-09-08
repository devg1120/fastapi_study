from functools import wraps
from typing import Any
from typing import Callable

from fastapi import FastAPI
from fastapi import Form
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.future import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://johndoe:secret@db/app")
                       ### {db-type}+{db-api}://{user}:{password}@{host}/{database}

Base = declarative_base()

class SomeInfo(Base):
    __tablename__ = "some_infos"
    id = Column(Integer, primary_key=True)
    desc = Column(String(255), nullable=True)

Base.metadata.create_all(engine)

ScopedSession = scoped_session(
    sessionmaker(bind=engine, future=True),
)

app = FastAPI()

def entrypoint(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def _entry_point(*args: Any, **keywords: Any) -> Any:
        session: Session = ScopedSession()
        try:
            result = func(*args, **keywords)
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        finally:
            ScopedSession.remove()
        return result
    return _entry_point

@app.post(
    "/info",
)
@entrypoint
def post_info(
    desc: str = Form(...),
) -> dict:
    session: Session = ScopedSession()
    with session.begin_nested():
        some_info = SomeInfo(
            desc=desc,
        )
        session.add(some_info)
        session.flush()
        return {
            "id": some_info.id,
            "desc": some_info.desc,
        }

