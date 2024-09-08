from setting import session
from user import User

data = session.query(User).all()

session.close()

#print(data)
for user in data:
    print(user.name)


