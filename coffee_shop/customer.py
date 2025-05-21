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

