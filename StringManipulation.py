# String Manipulation

print("I like \"Harry Potter\"")
print('I like "Harry Potter"')


# String Multiplication
print("+"+"-" * 50 + "+")
print(("|" + " " * 50 + "|\n") * 5, end="")
print("+"+"-" * 50 + "+")

# String Iteration
def VerticalPrint():
    str1 = input("Please enter a word\sentence: ")
    print("This input has " + str(len(str1)) + " characters")
    for i in range(0, len(str1), 1):
        print(str1[i])

VerticalPrint()

def ReverseString():
    # Reverse print a string
    str1 = input("Please enter a word: ")
    for i in range(len(str1) - 1, -1, -1):
        print(str1[i], end="")


ReverseString()










