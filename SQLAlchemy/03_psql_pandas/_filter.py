from setting import session
from user import User

users = session.query(User).filter(User.age == 60 ).all()
for user in users:
    print(user.name, user.age, user.email)
