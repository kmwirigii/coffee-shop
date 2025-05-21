from __future__ import annotations
from typing import List, Dict

class Customer:

    all: List[Customer] = []

    def __init__(self, name: str) -> None:
        self._orders: List[Order] = []
        self.name = name
        Customer.all.append(self)

    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1-15 characters")
        self._name = value

   
    def orders(self) -> List[Order]:
        return self._orders

    def coffees(self) -> List[Coffee]:
       
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee: Coffee, price: float) -> Order:
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide Coffee instance")
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

  

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Customer | None:
        if not isinstance(coffee, Coffee):
            raise ValueError("Must provide Coffee instance")

        if not coffee.orders():
            return None

       
        spending: Dict[Customer, float] = {}
        for order in coffee.orders():
            spending[order.customer] = spending.get(order.customer, 0) + order.price

        
        return max(spending.items(), key=lambda item: item[1])[0]


from .coffee import Coffee
from .order import Order
