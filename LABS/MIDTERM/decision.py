"""
=====================================================================
 TOPIC 01: The if Statement
=====================================================================
Instructions:
    - Read each problem carefully.
    - Look for the TODO comments and write your code there.
    - Do NOT change the input()/print() lines unless a TODO tells you to.
    - Test your code using the sample input/output provided.
=====================================================================
"""

# =====================================================================
# PROBLEM 1: Voting Eligibility Checker
# =====================================================================
# Scenario:
#   A barangay wants a simple program to check if a person
#   is old enough to vote.
#
# Task:
#   Ask the user for their age. If the age is 18 or older,
#   print "You are eligible to vote." Otherwise, print nothing.
#
# Sample Input: 20
# Sample Output: You are eligible to vote.
#
# Sample Input: 15
# Sample Output: (no message printed)
# =====================================================================

age = int(input("Enter your age: "))

# TODO: Write an if statement that prints "You are eligible to vote."
#       only when age is 18 or older.

if age >= 18:
    print("You are eligible to vote.")

# =====================================================================
# PROBLEM 2: Login Attempt Warning
# =====================================================================
# Scenario:
#   A simple login system needs to check if the user enters
#   the correct password.
#
# Task:
#   Store the correct password as "loop123" in a variable.
#   Ask the user to enter a password.
#   If the entered password does NOT match the correct password,
#   print "Incorrect password. Please try again."
#
# Sample Input: hello
# Sample Output: Incorrect password. Please try again.
#
# Sample Input: loop123
# Sample Output: (no message printed)
# =====================================================================

correct_password = "loop123"
entered_password = input("Enter your password: ")

# TODO: Write an if statement that prints the warning message
#       only when entered_password does NOT match correct_password.

if entered_password != correct_password:
    print("incorrect password. Please try again.")
# =====================================================================
# PROBLEM 3: Shopping Discount Alert
# =====================================================================
# Scenario:
#   A store wants to check if a customer's purchase qualifies
#   for a discount.
#
# Task:
#   Ask the user for their total purchase amount (float).
#   If the total is 2000 or more, print:
#       "Congratulations! You qualify for a 10% discount."
#
# Sample Input: 2500
# Sample Output: Congratulations! You qualify for a 10% discount.
#
# Sample Input: 800
# Sample Output: (no message printed)
# =====================================================================

total_purchase = float(input("Enter your total purchase amount: "))

# TODO: Write an if statement that checks if total_purchase is >= 2000
#       and prints the discount message.


# =====================================================================
# PROBLEM 4: Passing Grade Checker with String Comparison
# =====================================================================
# Scenario:
#   A teacher wants to check if a student's grade and remark match.
#
# Task:
#   Ask the user for their numeric grade (int).
#   Ask the user for their remark ("PASSED" or "FAILED").
#   If the grade is 75 or above AND the remark is NOT "PASSED",
#   print:
#       "Warning: Grade and remark do not match!"
#
# Sample Input: grade = 80, remark = FAILED
# Sample Output: Warning: Grade and remark do not match!
#
# Sample Input: grade = 80, remark = PASSED
# Sample Output: (no message printed)
# =====================================================================

grade = int(input("Enter your numeric grade: "))
remark = input("Enter your remark (PASSED/FAILED): ")

# TODO: Write an if statement using "and" that compares grade >= 75
#       with the remark string (use != for string comparison), then
#       prints the warning message when they don't match.

