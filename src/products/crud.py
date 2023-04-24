import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.products.config import get_data_database
from src.products.schemas import AddProduct
from src.products.models import Product


logger = logging.getLogger(name=__name__)


class ProductCRUD:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        try:
            self.__engine = create_engine("postgresql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s"\
                                % get_data_database(), echo=True)
        except Exception as ex:
            raise ConnectionError(f'''Don\'t creating engine database for
                                                \"{__class__}\"; Error: {ex}''')
        else:
            logger.info(f"Create engine is success!")
            try:
                self.__session = Session(bind=self.__engine)
            except Exception as ex:
                raise ConnectionError(f'''Don\'t open session for \'{__class__}\'
                                                    ; Error: {ex}''')
            else:
                logger.info(f"It\'s good opened session in {__class__}!")

    def add_product(self, product: AddProduct) -> None:
        product = Product(
            name=product["name"],
            price=product["price"]
        )
        try:
            self.__session.add(product)
            self.__session.commit()
        except Exception as ex:
            raise ConnectionError(f'''Don\'t addable \'{__class__}\'
                                    ; Error: {ex}''')

    def get_products(self) -> tuple[AddProduct] | bool:
        try:
            query = self.__session.query(Product).all()
        except Exception as ex:
            raise Exception(f'''Don\'t valid query for {__class__}
                            ; Error: {ex}''')
        else:
            logger.info("Query for gettable it\'s find!")

        if not query:
            return False

        products = []
        try:
            for product in query:
                products.append(AddProduct(**{
                    "name": product.name,
                    "price": product.price
                }))
        except Exception as ex:
            raise ValueError(f'''Values table {__class__[:-4]};
                                Except: {ex}''')

        return tuple(products)