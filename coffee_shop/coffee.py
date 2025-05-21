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





