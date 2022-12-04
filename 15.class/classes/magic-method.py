"""
python 3.6.5
python magic method
"""


class MagicMethod:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.len = 10

    def __add__(self, other):
        return MagicMethod(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"MagicMethod({self.x}, {self.y})"

    # def __repr__(self):
    #     return f"MagicMethod({self.x}, {self.y})"

    def __len__(self):
        return self.len

    def __call__(self):
        print("Hello! I am a MagicMethod")

    def __del__(self):  # destructor
        print("Goodbye! I am a MagicMethod")


v1 = MagicMethod(2, 10)
v2 = MagicMethod(5, -2)
v3 = v1 + v2
v3()  # Hello! I am a MagicMethod (__call__)
print(v3)
print(v3.x)
print(v3.y)
print(len(v3))
