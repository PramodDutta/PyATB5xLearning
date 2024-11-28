class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object_ref = Calc(3, 4)
object_ref2 = Calc(3, 4)
object_ref3 = Calc(3, 4)
object_ref4 = Calc(3, 4)

output = object_ref.sum()
output = object_ref.sub()
print(output)
