from __future__ import annotations
from typing import List

class Coffee:
    
    all: List[Coffee] = []

    def __init__(self, name: str) -> None:
        self._validate_name(name)
        self._name = name
        self._orders: List[Order] = []
        Coffee.all.append(self)

        @property
    def name(self) -> str:
        return self._name
    
    
    @name.setter
    def name(self, value: str) -> None:
       
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change coffee name after creation")
        self._validate_name(value)
        self._name = value

        
    def _validate_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        
        
    def orders(self) -> List[Order]:
        return self._orders

    def customers(self) -> List[Customer]:
        
        from .customer import Customer
        return list({order.customer for order in self._orders})
    
    
    def num_orders(self) -> int:
        return len(self._orders)

    def average_price(self) -> float:
        if not self._orders:
            return 0.0
        total_price = sum(order.price for order in self._orders)
        return round(total_price / len(self._orders), 2)







