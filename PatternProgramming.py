rowNum = 5

# The number of asterisk in each row equals to the row number
# Drawing 1 row of stars(5 stars)
for i in range(5): # For loop approach
    print("*", end=" ")

print("\r") # go to the next line


def Pyramid(rowNum):
    for i in range(1, rowNum + 1, 1):
        print("*" * i) # String multiplication approach

    # Reverse the triangle
    for i in range(rowNum - 1, 0, -1):
        print("*" * i)

def NumberPyramid(rowNum):
    """
    e.g. rowNum = 5
    1
    22
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    for i in range(1, rowNum + 1, 1):
        print((str(i) + " ") * i)




"""
1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
def NumPyramid2(rowNum):
    for j in range(2, rowNum + 2, 1):
        for i in range(1, j, 1):
            print(i, end=" ")

        print("\r")


"""
Multiplication table pattern
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
...
"""
print(1 * 1, end = " ")
print("\r")

print(2 * 1, end = " ")
print(2 * 2, end = " ")
print("\r")

print(3 * 1, end = " ")
print(3 * 2, end = " ")
print(3 * 3, end = " ")
print("\r")

for j in range(1, rowNum + 1, 1):
    # For each row repeat column times (row number)
    for i in range(1, j + 1, 1):
        print(i * j, end=" ")
    print("\r")

# first step, identify numbers that are changing, then replace it with a variable