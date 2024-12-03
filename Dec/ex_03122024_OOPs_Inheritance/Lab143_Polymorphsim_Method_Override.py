class Father:
    def home(self):
        print("1BHK")

class Pramod(Father):
    def home(self):
        print("3BHK")


p = Pramod()
p.home()

f = Father()
f.home()
