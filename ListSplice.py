# String Slicing
str1 = "KINGSLEYTAN"

# Kings
print(str1[0:5:1])

# Tan
print(str1[8::1])

# Print in reverse order
print(str1[::-1])
print(str1[10::-1])

# AYLGI
print(str1[9:0:-2])


# YELSG
print(str1[7:2:-1])


# Given any string that has at least 7 characters,
# Extract and join the last three characters
while True:
    ToContinue = input("Would you like to continue (Y/N): ")
    if ToContinue == "Y":
        testString = input("Enter a word that has at least 7 chars: ")
        if len(testString) >= 7:
            str1 = testString[0:3:1]
            str2 = testString[len(testString)-3::1]
            print(str1 + str2)
        else:
            print("Please enter a word that has at least 7 chars.")

    elif ToContinue == "N":
        print("Ok! See you later. Bye-Bye")
        break

    else:
        print("Don't try to be funny, only Y or N is accepted.")
