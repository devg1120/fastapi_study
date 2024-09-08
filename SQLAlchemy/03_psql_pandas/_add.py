# セッション変数の取得
from setting import session

# Userモデルの取得
from user import User

import datetime

# DBにレコードの追加
user = User()
user.name = '西草'
user.age = 60
user.email = 'devg1120@gmail.com'
user.created = datetime.datetime.now()
user.updated = datetime.datetime(year=2019, month=12, day=30, hour=14, minute=0, second=29)

session.add(user)


session.commit()

# usersテーブルのレコードを全て取得する
users = session.query(User).all()
for user in users:
    print(user.name)

