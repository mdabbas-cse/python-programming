import csv
import os


class readCsv:
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # validation for price and quantity
        assert price >= 0, f"Price must be greater than {price}"
        assert quantity >= 0, f"Quantity must be greater than {quantity}"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        readCsv.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_csv(cls):
        # csv file path
        path = os.path.dirname(__file__)
        with open(f"{path}/items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            readCsv(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    def __repr__(self):
        return f"Items({self.name}, {self.price}, {self.quantity})"
