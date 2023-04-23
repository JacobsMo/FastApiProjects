import logging

from argon2 import PasswordHasher

from .crud import UserCRUD
from .schemas import UserHashedPassword


logger = logging.getLogger(name=__name__)


def registration_user(name: str, email: str, password: str) -> None | bool:
    user = UserCRUD()
    hasher = PasswordHasher()
    hash = hasher.hash(password)
    try:
        added_user = user.add_user(UserHashedPassword(name=name,
                                                      email=email,
                                                      hashed_password=hash))
    except Exception as ex:
        logger.error(f"Add user error; Except: {ex}")
    else:
        logger.info(f"User successfully registration!")
        return added_user


def authentication_user(email: str, password: str) -> bool:
    user = UserCRUD()
    hasher = PasswordHasher()
    try:
        user_data = user.get_user(email=email)
    except Exception as ex:
        logger.error(f"Get user error: Except: {ex}")

    if user_data:
        try:
            return hasher.verify(user_data.hashed_password, password)
        except:
            return False
    else:
        return False

