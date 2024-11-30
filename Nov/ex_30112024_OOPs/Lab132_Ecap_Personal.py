class Home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var  = "child"


    def mom(self):
        print(self.__private_var)
        self.__wife()


    def __wife(self):
        print("Private Wife")


object_ref = Home()
object_ref.mom()
print(object_ref.public_var)
# object_ref.__wife()
# print(object_ref.__private_var) # 'Home' object has no attribute '__private_var'