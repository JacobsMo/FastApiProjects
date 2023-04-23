import logging
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import User, Item
from src.auth.config import get_data_database
from .schemas import UserHashedPassword, ResponseGetUser


logger = logging.getLogger(name=__name__)


class UserCRUD:

    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        try:
            self.engine = create_engine("postgresql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s"\
                            % get_data_database(), echo=True)
        except Exception as ex:
            raise ConnectionError(f'''Don\'t creating engine database for
                                    \"{__class__}\"; Error: {ex}''')

        try:
            self.session = Session(bind=self.engine)
        except Exception as ex:
            raise ConnectionError(f'''Don\'t open session for \'{__class__}\'
                                    ; Error: {ex}''')

    def add_user(self, hashed_password_user: \
                 UserHashedPassword) -> None | bool:
        if self.get_user(hashed_password_user.email) is not False:
            logger.debug(self.get_user(hashed_password_user.email))
            return False

        user = User(
            name=hashed_password_user.name,
            email=hashed_password_user.email,
            hashed_password=hashed_password_user.hashed_password,
            date_registration=date.today()
        )
        try:
            self.session.add(user)
            self.session.commit()
        except Exception as ex:
            raise ConnectionError(f'''Don\'t addable \'{__class__}\'
                                    ; Error: {ex}''')

        return True

    def get_user(self, email: str) -> ResponseGetUser | bool:
        try:
            answer = self.session.query(User).filter(User.email == email).all()
        except Exception as ex:
            raise Exception(f'''Don\'t valiable query for {__class__}
                            ; Error: {ex}''')

        try:
            return ResponseGetUser(**{
                "id": answer[0].id,
                "name": answer[0].name,
                "email": answer[0].email,
                "hashed_password": answer[0].hashed_password,
                "date_registration": str(answer[0].date_registration)
            })
        except:
            return bool(answer)
