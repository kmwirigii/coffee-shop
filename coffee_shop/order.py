from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .customer import Customer
    from .coffee import Coffee

    class Order:
    # Class-level list to store all orders
    all: list[Order] = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float) -> None:
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
