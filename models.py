from pydantic import BaseModel, Field

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

