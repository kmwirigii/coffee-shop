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

        
        customer._orders.append(self)
        coffee._orders.append(self)
        Order.all.append(self)

           @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change order price after creation")
        self._price = value

        
    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, value: Customer) -> None:
        if not hasattr(value, '_orders'):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value




