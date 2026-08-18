"""
Atienza, Gabriel Anthony H.
2258 6LOGPROG
Midterm: Python Activity 1: Using match-case
"""

#display the menu
print("===== MENU =====\nA. Add Student\nB. View Student\nC. Delete Student\nD. Exit\n")

#input section
choice = input("Enter your choice: ") #assigns the input to the variable choice
choice = choice.upper() #makes sure the variable is uppercase using uppercase function

#match case
match choice:
    case "A": #if the choice is A, print Adding Student...
        print("Adding Student...")
    case "B": #if the choice is B, print Viewing Student...
        print("Viewing Student...")
    case "C": #if the choice is C, print Deleting Student...
        print("Deleting Student...")
    case "D": #if the choice is D, print Exiting Program...
        print("Exiting Program...")
    case _: #else if input is none of the options, print Invalid Choice
        print("Invalid Choice!")
