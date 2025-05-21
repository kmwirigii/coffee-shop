import pytest
from coffee_shop.customer import Customer 
from coffee_shop.coffee import Coffee      
from coffee_shop.order import Order       

class TestCustomer:
    def test_customer_creation(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
    
    def test_invalid_name(self):
        with pytest.raises(ValueError):   
            Customer("") 
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")
    
    def test_create_order(self):
        customer = Customer("Gilly")  
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 5.0)
        assert order in customer.orders()
        assert order in coffee.orders()