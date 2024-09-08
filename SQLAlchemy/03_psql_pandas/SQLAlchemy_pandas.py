
from sqlalchemy import create_engine, Column, table, Integer, String, DATETIME
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from user import User
from sqlalchemy.sql import select
import pandas as pd

DATABASE = "postgresql://postgres:postgres@localhost:5432/testdb2"
Base = declarative_base()

def main():
    # Create engine for SQLite
    #engine = create_engine(f'sqlite://{file_path}', echo=True)
    engine = create_engine(DATABASE, echo=False)
    
    # Create session
    #SessionClass = sessionmaker(engine)
    #session = SessionClass()

    
    # Target
    user_name = "西草"
    user_age = 20

    # SELECT
    sql_statement1 =  select(
                            User.id,
                            User.name, 
                            User.age,
                            User.email,
                            User.created,
                            User.updated,
                        )
    
    sql_statement2 = (
                        select(
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
                    )

   
    
    sql_statement3 = "SELECT name, email, age, created, updated  FROM users;"

    sqls = sql_statement2
    ## Get row SQL
    print("============== row SQL =================")
    print(sqls)
    print("========================================")

    df = pd.read_sql_query(sql=sqls, con=engine)
    print("=========== query result ===============")
    print(df)
    print("========================================")

    #for user in users:
    #    print(f"id:{user.id}, name:{user.name}, age:{user.age} email:{user.email} {user.created} {user.updated}")
        
    # DBと切断
    #session.close()

    # エンジン破棄
    engine.dispose()

if __name__ == "__main__":
    main()

