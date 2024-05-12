# List
# Empty list - []

foodList = ["MilkTea", "Sushi", "Pizza", "SundaeCone"]



for i in range(0, len(foodList), 1):
    print(foodList[i], end=" ** ")

print("\r")



for eachFood in foodList:
    print(eachFood, end=" ** ")

print("\r")

print(foodList[::-1])
for i in range(len(foodList) -1, -1, ):
    print(foodList[i], end=" ")
