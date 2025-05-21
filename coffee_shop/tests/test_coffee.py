import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order 

class TestCoffee:
    def test_average_price(self):
        coffee = Coffee("Latte")
        customer = Customer("Charlie")
    
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 7.0)
        assert coffee.average_price() == 6.0