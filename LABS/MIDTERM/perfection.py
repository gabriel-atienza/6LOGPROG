"""
Second Perfection
by CodeChum Admin

Write a program that takes an integer num as input and does the following checks:

If num is a perfect square (i.e., the square of an integer) and a perfect cube (i.e., the cube of an integer), print "Perfect in every way"
If num is a perfect cube and divisible by 2, print "Perfect in even cubes"
If num is a perfect cube and not divisible by 2, print "Perfect in an odd way"
If it does not conform to any of the conditions, print "Nothing special"
"""

num = int(input("Enter an integer: "))

square = round(num ** 0.5)
cube = round(num ** (1/3))

is_square = ((square * square) == num)
is_cube = ((cube * cube * cube) == num)

if is_square == True and is_cube == True:
    print("Perfect in every way")
elif is_cube == True:
    if num % 2 == 0:
        print("Perfect in even cubes")
    else:
        print("Perfect in an odd way")
else:
    print("Nothing special")


num = int(input("Enter an integer: "))

"""
# Check if num is a perfect square
is_perfect_square = False
for i in range(1, num + 1):
    if i * i == num:
        is_perfect_square = True
        break

# Check if num is a perfect cube
is_perfect_cube = False
for i in range(1, num + 1):
    if i * i * i == num:
        is_perfect_cube = True
        break

if is_perfect_square and is_perfect_cube:
    print("Perfect in every way")
elif is_perfect_cube and num % 2 == 0:
    print("Perfect in even cubes")
elif is_perfect_cube and num % 2 != 0:
    print("Perfect in an odd way")
else:
    print("Nothing special")

"""