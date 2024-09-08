
from setting import session
from user import User
import datetime


f = open('users_data.csv', 'r')
for line in f:
    line_ = line.rstrip('\r\n')
    if line_ == "":
        continue
    if line_[0] == '#':
        continue
    print(line_)
    data = line_.split(',')
    print(data)
    user = User()
    user.name = data[0].strip()
    user.age = int(data[1].strip())
    user.email = data[2].strip()
    user.created = datetime.datetime.strptime(data[3].strip(), '%Y/%m/%d %H:%M:%S')
    user.updated = datetime.datetime.strptime(data[4].strip(), '%Y/%m/%d %H:%M:%S')
    session.add(user)

f.close()

# DBにレコードの追加
#user = User()
#user.name = '西草'
#user.age = 60
#user.email = 'devg1120@gmail.com'
#user.created = datetime.datetime.now()
#user.updated = datetime.datetime(year=2019, month=12, day=30, hour=14, minute=0, second=29)
#
#session.add(user)

session.commit()

data = session.query(User).all()
session.close()

for user in data:
    print(user.name, 
           user.age,
           user.email,
           user.created,
           user.updated,
            )

