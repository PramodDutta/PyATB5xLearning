class Parent:
    gold = "2kg"

    def __init__(self):
        print("DC - Parent")

    def BHK2(self):
        print("2BHK")


class Child(Parent):

    def __init__(self):
        print("DC - Child")

    diamond = "Diamond"

    def BHK3(self):
        print("3BHK")

child_object= Child()
print(child_object.gold)
child_object.BHK2()


father_obect_ref = Parent()
father_obect_ref.BHK2()
# father_obect_ref.BHK3()