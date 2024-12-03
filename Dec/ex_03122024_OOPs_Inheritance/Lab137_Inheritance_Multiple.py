# Multiple Inheritance

class A:
    def method(self):
        return "Method A"


class B:
    def method(self):
        return "Method B"


class C(B, A):
    pass


c = C()
print(c.method())
