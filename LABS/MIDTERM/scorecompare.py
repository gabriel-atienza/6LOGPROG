"""
Exam Result Comparison
by CodeChum Admin

Write a program that takes two inputs: score1 and score2, both of type float. It should compare the two scores and print a message based on the following rules:

If score1 is greater than score2 and score1 is greater than 80, print "Excellent!"
If score1 is greater than score2 but score1 is not greater than 80, print "Good job!"
If score1 is not greater than score2, print "Keep up the good work!"
"""

score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))

if score1 > score2:
    if score1 > 80:
        print("Excellent!")
    else:
        print("Good job!")
else:
    print("Keep up the good work!")