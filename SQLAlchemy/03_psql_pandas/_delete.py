from setting import session
from user import User

user = session.query(User).first()

session.delete(user)
session.commit()

session.close()
