from pydantic import BaseModel, Field
from pydb import Model, StringField, FloatField, IntField

# Pydantic Schemas for Validation
class Menu(BaseModel):
    id: int = Field(gt=0, description="The menu ID must be greater than zero.")
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(ge=0.0, description="The price must be non-negative.")
    description: str = Field(max_length=500)
    image: str

class Order(BaseModel):
    orderId: int = Field(gt=0, description="The order ID must be greater than zero.")
    item: int = Field(gt=0, description="The menu item ID must be greater than zero.")
    qty: int = Field(gt=0, description="The quantity must be at least 1.")

# PyDB ORM Models
class MenuDB(Model):
    name = StringField(required=True)
    price = FloatField(default=0.0)
    description = StringField(required=False)
    image = StringField(required=False)

class OrderDB(Model):
    item = IntField(required=True)
    qty = IntField(default=1)

