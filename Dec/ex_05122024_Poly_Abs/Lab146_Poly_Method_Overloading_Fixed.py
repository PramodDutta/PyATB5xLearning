# Method Overloading is Not Supported - Python
class Calc:
    def sum(self, *args):
        for a in args:
            print(a)

# *args - multiple values

calc_ref = Calc()
calc_ref.sum(1)
print( "  --- ")
calc_ref.sum(1, 2)
print( "  --- ")
calc_ref.sum(1, 2, 3)

