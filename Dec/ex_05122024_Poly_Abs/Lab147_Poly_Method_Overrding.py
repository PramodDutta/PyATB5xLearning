class Parent:
    def home(self):
        print("2BHK")


class Son(Parent):
    def town(self):
        print("10 BHK")

    def home(self):
        print("3BHk")


ob_Ref = Son()
ob_Ref.home()
ob_Ref.town()
