import logging

from pydantic import BaseModel, Field, validator, ValidationError


logger = logging.getLogger(name=__name__)


class AddProduct(BaseModel):

    name: str = Field(max_length=50)
    price: int

    @validator(name)
    @classmethod
    def validator_name(cls, value):
        if not isinstance(value, str):
            raise ValidationError("Name it not string!")

        return value

    @validator(price)
    @classmethod
    def validator_price(cls, value):
        if not isinstance(value, int):
            raise ValidationError("Price it not string!")

        if value < 0 or value > 1000000:
            raise ValidationError("Price it not correctly!")

        if value == 0:
            logger.warning("Price for product is 0, may be you error?")

        return value