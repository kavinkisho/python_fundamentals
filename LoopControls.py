# for loop
# It is used when we know specifically the number of repetitions
# for i in range(0, 5, 1):
#    print("🍪")

# while loop
# It is used when we're uncertain about the number of iterations
# But we know the condition for which the loop has to remain active

import time

cookieCount = 0
while True:
    cookieCount = cookieCount + 1 #Change cookieCount by +1
    print("🍪"  + " - " + str(cookieCount))
    if cookieCount == 5:
        pass
    if cookieCount > 99:
        print("You win")
        break   # Terminate the loop immediately
    # The continue statement exits the current iteration
    # and starts a new iteration in the same loop
    if cookieCount < 50:
        continue
    print("You are getting close to winning!")
    time.sleep(0.1)