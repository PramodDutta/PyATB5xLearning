# Method Overloading
class Dog:
    def bark(self):
        print("Dog is Barking")

    def bark(self, breed):
        print(f"Dog with {breed} is barking")


d = Dog()
