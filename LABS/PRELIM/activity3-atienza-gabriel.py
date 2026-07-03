#6LOGPROG Laboratory Exercise 3
#Atienza, Gabriel Anthony H.

#variables
english_grade = int(input("Enter your grade for English: ")) #asks the user for their english grade
math_grade = int(input("Enter your grade for Math: ")) #asks the user for their math grade
science_grade = int(input("Enter your grade for Science: ")) #asks the user for their science grade
filipino_grade = int(input("Enter your grade for Filipino: ")) #asks the user for their filipino grade
panlipunan_grade = int(input("Enter your grade for Araling Panlipunan: ")) #asks the user for their araling panlipunan grade

#average grade computation of the five subjects
average = (english_grade + math_grade + science_grade + filipino_grade + panlipunan_grade) / 5

#if else section
if average >= 75:  #compares average grade to passing grade
    print("Average: ", float(average)) #prints the string average grade with the average result
    print("Result: PASSED") #prints passed message
else: #else if user is failing
    print("Average: ", float(average)) #print the string average grade with the average result
    print("Result: FAILED") #prints the string failed
