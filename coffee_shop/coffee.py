from __future__ import annotations
from typing import List

class Coffee:
    
    all: List[Coffee] = []

    def __init__(self, name: str) -> None:
        self._validate_name(name)
        self._name = name
        self._orders: List[Order] = []
        Coffee.all.append(self)
