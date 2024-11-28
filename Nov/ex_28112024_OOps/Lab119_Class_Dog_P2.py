class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None


    def __init__(self, name, breed):
        print("PC")
        self.name = name
        self.breed = breed

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleep -> " + self.name )

    def talk(self):
        pass


# Object Ref
chow_ref = Dog("chow","mastiff")
print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))


mow_ref = Dog("mow","husky")
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))


