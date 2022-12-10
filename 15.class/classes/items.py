class Items:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: int):
        # validation for price and quantity
        assert price >= 0, f"Price must be greater than {price}"
        assert quantity >= 0, f"Quantity must be greater than {quantity}"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate
