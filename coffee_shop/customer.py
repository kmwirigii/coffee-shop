from __future__ import annotations
from typing import List, Dict

class Customer:
    
    all: List[Customer] = []

    def __init__(self, name: str) -> None:
        self._orders: List[Order] = []
        self.name = name
        Customer.all.append(self)
