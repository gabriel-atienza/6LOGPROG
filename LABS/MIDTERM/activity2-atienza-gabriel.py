"""
Atienza, Gabriel Anthony H.
2258 6LOGPROG
Midterm: Python Activity 2: Subject Enrollment System using match-case
"""

#display the menu
print("===== SUBJECT ENROLLMENT =====")
print("1 - Programming Fundamentals")
print("3 - Computer Networking")
print("4 - Web Development")
print("5 - Object-Oriented Programming\n")

#input section
subject_num = int(input("Enter your choice: ")) #assigns the input to the int variable

print("") #print blank space
      
#match case
match subject_num:
    case 1: #if the choice is 1, print the following
        print("Subject: Progrraming Fundamentals")
        print("Instructor: Mr. Santos")
        print("Room: Lab 101")
    case 2: #if the choice is 2, print the following
        print("Subject: Database Management")
        print("Instructor: Ms. Cruz")
        print("Room: Lab 202")
    case 3: #if the choice is 3, print the following
        print("Subject: Computer Networking")
        print("Instructor: Mr. Garcia")
        print("Room: Lab 303")
    case 4: #if the choice is 4, print the following
        print("Subject: Web Development")
        print("Instructor: Ms. Reyes")
        print("Room: Lab 204")
    case 5: #if the choice is 5, print the following
        print("Subject: Object-Oriented Programming")
        print("Instructor: Mr. Dela Cruz")
        print("Room: Lab 105")
    case _: #else if input is none of the options, print invalid subject selection
        print("Invalid subject selection")
