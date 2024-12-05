# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.

class O:
    @staticmethod
    def sum(a, b):
        return a + b

    def sub(self,a,b):
        return a-b


obj_O = O()
result = obj_O.sub(3,4)
print(result)
print(" -- ")

print(O.sum(3,4))