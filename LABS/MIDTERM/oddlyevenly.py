"""
Oddly or Evenly
by CodeChum Admin

Write a program that takes an integer input, number. It should check the number according to the following rules and print the corresponding message:

If the number is odd, it should print "Odd number"
If the number is odd and divisible by 3, it should print "Oddly divisible by 3"
If the number is even, it should print "Even number"
If the number is even and divisible by 4, it should print "Evenly divisible by 4"
"""

num = int(input("Enter an integer: "))

if num % 2 == 1:
    if num % 3 == 0:
        print("Oddly divisible by 3")
    else:
        print("Odd number")
else:
    if num % 4 == 0:
        print("Evenly divisible by 4")
    else:
        print("Even number")