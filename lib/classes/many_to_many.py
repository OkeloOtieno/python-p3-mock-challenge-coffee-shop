class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, 'name'):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name) >= 3:
                    self._name = new_name
                else:
                    ValueError("Name must be at least 3 characters")
            else:
                TypeError("Name must be a string")

    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return sum(1 for order in Order.all if order.coffee == self)
    
    def average_price(self):
        return sum(order.price for order in self.orders()) / self.num_orders()

class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 1 <= len(new_name) <= 15:
                self._name = new_name
            else:
                ValueError("Invalid name")
        else:
            TypeError("Invalid name")


    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if hasattr(self, "price"):
            AttributeError("Price cannot be changed")
        else:
            if isinstance(new_price, float):
                if 1.0 <= new_price <= 10.0:
                    self._price = new_price
                else:
                    ValueError("Price must be between 1.0 and 10.0")
            else:
                TypeError("Price must be of type float")
                


    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        if not isinstance(new_customer, Customer):
            raise TypeError("Customer must be of type Customer")
        else:
            self._customer = new_customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee):
        if not isinstance(new_coffee, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        else:
            self._coffee = new_coffee
