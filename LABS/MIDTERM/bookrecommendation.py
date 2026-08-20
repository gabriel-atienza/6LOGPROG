"""
Book Recommendation
by CodeChum Admin

Write a program that takes a reader's age and genre preference as input and recommends a book based on the following conditions:

If the reader is between 8 and 12 years old (inclusive):
If they prefer adventure, print "The Adventures of Tom Sawyer".
If they prefer mystery, print "Nancy Drew: The Secret of the Old Clock".
If the reader is between 13 older:
If they prefer fantasy, print "Harry Potter and the Sorcerer's Stone".
If they prefer science fiction, print "Ender's Game".
If the reader does not meet any of the above criteria, print "No recommendation available".
"""

age = int(input("Enter your age: "))
genre = input("Enter your genre preference (a for adventure, m for mystery, f for fantasy, s for science fiction): ")

if age >= 8 and age <= 12:
    if genre == "a":
        print("The Adventures of Tom Sawyer")
    elif genre == "m":
        print("Nancy Drew: The Secret of the Old Clock")
elif age >= 13:
    if genre == "f":
        print("Harry Potter and the Sorcerer's Stone")
    elif genre == "s":
        print("Ender's Game")
else:
    print("No recommendation available")


