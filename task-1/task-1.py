import math


def makeArrayOfNumbers(generalArray, tmpArray):
    try:
        number = ("".join(tmpArray))
        generalArray.append(float(number))
        tmpArray.clear()
    except ValueError:
        pass


line = input("Enter the string: ")

## Create a new string
numbers = []
tmpNumbers = []
string = []

for letter in list(line):
    try:
        string.append(str(letter))
        if string[-1] == ' ' or string[-1].isalpha():
            makeArrayOfNumbers(numbers, tmpNumbers)
        if float(string[-1]) or float(string[-1]) == 0:
            string.pop()
            tmpNumbers.append(str(letter))
    except (ValueError, NameError):
        pass
makeArrayOfNumbers(numbers, tmpNumbers)

string = "".join(string)
newString = string

## Create a new changed string
string = string.split()
for i in range(len(string)):
    if len(string[i]) > 1:
        someWord = string[i]
        string[i] = someWord[0].upper() + someWord[1:-1] + someWord[-1].upper()
newChangedString = " ".join(string)

## Alter an array of numbers
changedNumbers = []

try:
    maxValue = max(numbers)
    position = numbers.index(maxValue) + 1
except ValueError:
    pass

for i in range(len(numbers)):
    if numbers[i] == maxValue and position == i + 1:
        changedNumbers.append(numbers[i])
    if numbers[i] != maxValue and position != i + 1:
        changedNumbers.append(pow(numbers[i], i))

## Output result
print(line)
print(newString)
print(numbers)
print(newChangedString)
print(changedNumbers)
