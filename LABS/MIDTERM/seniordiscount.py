"""
Senior Citizen Discount
by CodeChum Admin

Write a program that takes two inputs: an int age and a float income. It should determine whether a person is eligible for a senior citizen discount based on the following rules and print the corresponding eligibility message:

If age is greater than or equal to 60 and income is less than 10000, print "Eligible for senior citizen discount"
If age is greater than or equal to 60 but income is 10000 or more, print "Not eligible for senior citizen discount"
If age is less than 60, print "Not eligible for senior citizen discount"

"""

age = int(input("Enter your age: "))
income = float(input("Enter your income: $"))

if age >= 60:
    if income < 10000:
        print("Eligible for senior citizen discount")
    else:
        print("Not eligible for senior citizen discount")
else:
    print("Not eligible for senior citizen discount")