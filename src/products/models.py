from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.products.config import get_data_database


base = declarative_base()
engine = create_engine("postgresql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s" \
                       % get_data_database())


class Product(base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Integer, nullable=False)


base.metadata.create_all(engine)