# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1



num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor): "))

quotient = num1 // num2  # Using floor division to get the quotient
remainder = num1 % num2   # Using modulo to get the remainder

#divmod()


print(f"Quotient (Q) -> {quotient}")
print(f"Remainder (R) -> {remainder}")