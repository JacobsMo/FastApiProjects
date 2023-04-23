from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.auth.config import get_data_database


base = declarative_base()
engine = create_engine("postgresql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s"\
                        % get_data_database(), echo=True)


class User(base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    date_registration = Column(Date, nullable=False)


base.metadata.create_all(engine)