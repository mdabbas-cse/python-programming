from classes.student import Student
from classes.items import Items

student = Student("John", 123)
course = student._get_course("Math")
print(student)
print(course)

item = Items("Book", 10, 5)
price = item.calculate_total_price()
print(f"Total price is {price}")

"""
those are the attributes of the class Items and the object item are helpful for debugging
# get all the attributes for class label
print(Items.__dict__)
# get all the attributes for object label
print(item.__dict__)
"""
discount = item.apply_discount()
print(f"Discount price is {discount}")

# item 2
print("+++++this is item 2+++++")
item2 = Items(
    "Phone", quantity=7, price=100
)  # this is the way to pass the keyword arguments
price2 = item2.calculate_total_price()
print(f"Total price is {price2}")
item2.pay_rate = 0.9  # this is the way to change the class attribute
discount2 = item2.apply_discount()
print(f"Discount price is {discount2}")

print(Items.all)
