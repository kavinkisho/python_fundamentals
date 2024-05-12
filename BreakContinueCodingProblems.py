testString = "GhostTownOhio"

# for loop with the range() function
for i in range(0, len(testString),1):
    print(testString[i], end="👻 ")

print("\r")

# for-each loop in Python
# eachChar represents the character in the current iteration
# as we iterate through the testString
for eachChar in testString:
    print(eachChar, end="👻 ")


print("\r")

# Question 1 - Print every character in the testString except for letter "O" "o"
#               USING THE FOR-EACH LOOP APPROACH AND CONTINUE STATEMENT
for eachLetter in testString:
    if eachLetter == "O" or eachLetter == "o":
        continue # To start a new iteration immediately
    print(eachLetter, end=" ")


print("\r")

# Question 2 - To count the occurances of letter "O" "o" in the testString
# Use for each-loop, declare a new variable "count" to keep the count
count = 0
for eachLetter in testString:
    if eachLetter == "O" or eachLetter == "o":
        count = count + 1
print(count)

print("\r")

# Question 3 - To print every character before the second letter "O" or "o"
# Cut off at the second letter "O" or "o"
# for each loop, break, count variable
count = 0
for eachLetter in testString:
    if eachLetter == "O" or eachLetter == "o":
        count = count + 1
    if count == 2:
        break
    print(eachLetter, end=" ")

print("\r")

# Question 4 - Reverse print all characters before the second letter of "O" or "o"
# Example
# testString = "GhostTownOhio"
# Output = T t s o h G

count = 0
temp_str = ""
for eachLetter in testString:
    if eachLetter == "O" or eachLetter == "o":
        count = count + 1
    if count == 2:
        break

    # Add each letter into the temp-str
    temp_str = temp_str + eachLetter

print(temp_str[::-1])