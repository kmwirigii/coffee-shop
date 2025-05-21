import pytest
from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

class TestOrder:
    def test_order_creation(self):
        customer = Customer("David")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 4.5)
        assert order.price == 4.5