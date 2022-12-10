from items import Items


class Phones(Items):
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int = 0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones must be greater than {broken_phones}"
        self.broken_phones = broken_phones

    def count_broken_phones(self):
        return self.broken_phones


phones = Phones("iPhone", 1000, 5, 1)
total_price = phones.calculate_total_price()
print(f"Total price is {total_price}")
discount = phones.apply_discount()
print(f"Discount price is {discount}")
broken_phones = phones.count_broken_phones()
print(f"Broken phones are {broken_phones}")

print(Items.all)
print(phones.all)
