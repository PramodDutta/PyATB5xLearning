# Method Overloading


class MathUtils:
    # Method - overloading - Not
    # supported!
    def add(self, a=10, b=20):
        return a + b

    # def add(self, a=1, b=1, c=1):
    #     return a + b + c
    #
    # def add(self, a=0, b=0, c=0, d=0):
    #     return a + b + c + d


math = MathUtils()
op1 = math.add(1, 2)