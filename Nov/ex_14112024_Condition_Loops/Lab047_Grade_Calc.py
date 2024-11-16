# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 ->  O/p -> str -> A or B....

score = int(input("Enter your score\n"))

# score >=90 and score <=100 -> "A"
# score >=80 and scroe <=89 -> "B"

if score >= 90 and score <= 100:
    print("You grade is ", "A")
elif score >= 80 and score <= 89:
    print("You grade is ", "B")
elif score >= 70 and score <= 79:
    print("You grade is ", "C")
elif score >= 60 and score <= 69:
    print("You grade is ", "D")
elif score >= 100 and score <= -1:
    print("You are  Superman!!, you can't get a grade!! 0:)")
else:
    print("You grade is ", "F")
