import random

list = []

# Exercise 1
for i in range(30):
    list.append(random.randint(-100, 100))
maxValue = max(list)
position = list.index(maxValue) + 1

print(list)
print("\nA max value of list:", maxValue, "\nIts position:", position, "\n")

oddList = []
for i in range(len(list)):
    if list[i] % 2 != 0:
        oddList.append(list[i])
if oddList == []:
    print("\nNo one odd number!")
print(sorted(oddList, reverse=True))

# Exercise 2
for i in range(len(list) - 1):
    if list[i] < 0 and list[i] == list[i + 1]:
        print("\nCouple of negative numbers:", list[i], list[i + 1])
