# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))


def sum_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3


result = sum_three(num1, num2, num3)
print(result)


result2 = sum_three()
result2 = sum_three(10)
result2 = sum_three(10,20)
result2 = sum_three(10,20,30)
print(result2)
