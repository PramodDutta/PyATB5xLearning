# Write a program to take a user age and
# let him know if he can go the club.
# 21

# Logic Building Formula

# Step 1
# user input i/p -> data type -> int
# o/p -> String -> user if he can go or not.

# Step 2. Rough logic (  brute force)
# age  > 21 -> print can go
# age < 21 -> print can't go

# Step 3. write the logic
age = input("Enter you age\n")
age = int(age)

if age >= 21:
    print("can go to Club!")
else:
    print("Can't go with this age")


# Step 4.  Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC
# Age which is valid. > 130



# Step 5.  Optimize the code.
# Handle all the edges.