gameList = ["Minecraft", "Roblox"]
gameList.append("Bawl Stars")
#print(gameList)

gameList.insert(1, "Call Of Duty")
#print(gameList)

gameList.insert(0, "Valorant")
#print(gameList)


import time
def AnimatedTriangle():
    numList1 = []
    while True:
        for i in range(1,11, 1):
            numList1.insert(0, i)
            print(numList1)
            time.sleep(0.05)

        for i in range(len(numList1) - 1):
            del numList1[-1]
            print(numList1)
            time.sleep(0.05)


numList1 = [5, 18, 89, 1, 200, 16, 20, 201, -100]

def our_max_function(anyList):
    curr_max = 0
    for eachNum in anyList:
        if eachNum > curr_max:
            curr_max = eachNum
    return curr_max
print(max(numList1))

print(our_max_function(numList1))

def our_min_function(anyList):
    curr_min = our_min_function(anyList)
    for eachNum in anyList:
        if eachNum < curr_min:
            curr_min = eachNum
    return curr_min



def Sum(anyList):
    basket = 0
    for eachNum in anyList:
        basket = basket + eachNum # Change basket by +eachNum
    return basket



print(Sum([3,4,5,6, -18]))




def SumAvg(anyList):
    return Sum(anyList) / len(anyList)


"""
estList = [1, 2, 8, 5, 10, 2]
output: [1, 2, 8, 5, 10
Algorithm:
1.Define an empty list
2.Apply a for loop and iterate the testList
3.If the item is not already in the empty list, add it to the empty list
"""

def remove_duplicates(testList):
    empty_list = []
    for eachNum in testList:
        if eachNum not in empty_list:
            empty_list.append(eachNum)
    return empty_list

print("The list after removing duplicates is: ", remove_duplicates([1, 4, 4, 1]))



# In-built Python sorting function
testList = [100, 86, 69, 1, 4, 1000, -8]
sorted_list = sorted(testList, reverse=True)
print(sorted_list)

# Build a function that returns the second largest number in the list
# Use sorted() function
def second_largest(anyList):
    return sorted(anyList, reverse=True)[1]

print(second_largest([4,5,9,10,11]))


print(sorted(['e','a','i','u','o']))