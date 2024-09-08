from setting import session
from user import User

user = session.query(User).first()
user.name = '次郎'

session.commit()

session.close()

