# Take input and create a class in python

class Person:

    def __init__(self):
        print("I will be called")
        self.name = input("Enter the name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone\n")
        self.occupation = input("Enter your occupation\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}",
              f"occupation is {self.occupation}")


person1 = Person()
person1.name_of_the_function_to_display()