"""
Write a Python program to add 'ing' at the end
of a given string(length should be at least 3).
If the given string already ends with 'ing',
add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
"""
# Example:
# work - working
# doing - doingly
# oh - oh

# A parameterised function
def add_string(testString):
    if len(testString) > 2:
        if testString[-3::1] == "ing":
            testString = testString + "ly"
            print(testString)
        else:
            testString = testString + "ing"
            print(testString)
    else:
        print(testString)

# Question 2
# Given any String of odd length greater than 7,
# print out the middle 3 characters line by line
# testString = "Swiss Cottage1"
# Output: C
#         o
#         t

def mid3(testString):
    # Check if the number is odd or even
    # using the modules operator
    if len(testString) % 2 == 1 and len(testString) > 7:
        middleIndex = int((len(testString) - 1) / 2)
        print(testString[middleIndex - 1])
        print(testString[middleIndex])
        print(testString[middleIndex + 1])

# Question 3
# Remove the n-th index character from a none,pty string

# A parameterised with two parameters
def remove_char(testString, n):
    first_part = testString[:n:1]
    second_part = testString[n + 1::1]
    print(first_part + second_part)


# Question 4
# Write a Python program to change a given
# string to a new string where the first and last chars
# have been exchanged.
def swap_first_last(testString):
    print(testString[-1] + testString[1:-1:1] + testString[0])


# Queston 5
# Write a python program to remove
# characters that hav odd index i a given string

def remove_odds(testString):
    for i in range(0, len(testString), 1):
        print(testString[i])

remove_odds("Timothy")





