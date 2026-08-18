"""
Atienza, Gabriel Anthony H.
2258 6LOGPROG
Python Activity 3: Multiplication Table Using a for Loop
"""

# Input
num = int(input("Enter a number: ")) #asks the user for a number and assigns to num
print("") #prints a blank space

# Loop
for i in range(1, 11): #runs the loop until i is 10
    #prints the multiplication table from 1 to 10
    #takes the input variable and multiplies it to the variable i
    #variable i goes from 1 to 10
    print(f"{num} x {i} = {num * i}") #output is a multiplication table
