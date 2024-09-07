#POSTGRES_USER=postgres
#POSTGRES_PASSWORD=postgres
#POSTGRES_SERVER=db
#POSTGRES_PORT=5432
#POSTGRES_DB=postgres

#DATABASE_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# path = 'sqlite:///db.sqlite3'
# path = 'mysql+pymysql://root:@127.0.0.1:3306/alembic_sample'
#path=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
 
path = "postgresql://postgres:postgres@localhost:5432/testdb"


# Engine の作成
Engine = create_engine(
  path,
  #encoding="utf-8",
  echo=False
)
Base = declarative_base()



