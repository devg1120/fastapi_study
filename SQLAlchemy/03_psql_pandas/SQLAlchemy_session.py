
from sqlalchemy import create_engine, Column, table, Integer, String, DATETIME
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from user import User
# from sqlalchemy.sql import select
# import pandas as pd

DATABASE = "postgresql://postgres:postgres@localhost:5432/testdb2"
Base = declarative_base()

def main():
    # Create engine for SQLite
    #engine = create_engine(f'sqlite://{file_path}', echo=True)
    engine = create_engine(DATABASE, echo=False)
    
    # Create session
    SessionClass = sessionmaker(engine)
    session = SessionClass()

    # Target
    user_name = "system"
    user_age = 40

    # SELECT
    users = session.query(
                            User.id,
                            User.name, 
                            User.age,
                            User.email,
                            User.created,
                            User.updated,
                        ).filter(
                            (User.name == user_name) &
                            (User.age >= user_age) 
                        ).limit(10)

    for user in users:
        print(f"id:{user.id}, name:{user.name}, age:{user.age} email:{user.email} {user.created} {user.updated}")
        
    # DBと切断
    session.close()

    # エンジン破棄
    engine.dispose()

if __name__ == "__main__":
    main()

