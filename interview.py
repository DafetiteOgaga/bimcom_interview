#!/usr/bin/env python3

# import os, autoPyandBat
# os.chdir("c:/Users/pc/Desktop/python_scripts_dafe")
# autoPyandBat.createPyAndBat()


from random import randint


MONDAY = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
TUESDAY = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE"
WEDNESDAY = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE"
THURSDAY = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
FRIDAY = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
WEEK = MONDAY + "," + TUESDAY + "," + WEDNESDAY + "," + THURSDAY + "," + FRIDAY

weekList = [color.lstrip() for color in WEEK.split(",")]
totalColor = len(weekList)
print("number of colors=", totalColor)
print()
count = 0
mainDictColAndVal = {}
for color in weekList:
    if color in mainDictColAndVal.keys():
        continue
    numAppearance = weekList.count(color)
    mainDictColAndVal.setdefault(color, numAppearance)
    print(f"color = {color}")
    print()
    print(f"numAppearance = {numAppearance}")
    print()

    #####################################################################################
    numString = ""
    for col in weekList:
        if col == color:
            res = 1
        else:
            res = 0
        numString += str(res)
    print(f"numString = {numString}")
    print()
    numList = [numItem for numItem in numString]
    listSize = len(numList)
    finalResult = ""
    for num in range(listSize-2):
        if numList[num] == numList[num + 1] and numList[num + 1] == numList[num + 2]:
            result = numList[num]
        else:
            result = "0"
        finalResult += result
    print("finalResult", finalResult)
    print("00" + finalResult)
    print()
    #####################################################################################

    count += 1
print("count", count)####
# print("sumCount", sumCount)####
print("totalColor", totalColor)####
# print("sumAppearance", sumAppearance)####
# print("colorSum", colorSum)####
# print("colorList", colorList)####
# print("appearanceList", appearanceList)####

## no.1
## Which color of shirt is the mean color?
def meanVal():
    meanVal = round(totalColor/count)
    return f"mean color = {meanVal}"



## no.2
## Which color is mostly worn throughout the week?
def mostWornColor():
    return f"mostly worn color = {max(mainDictColAndVal.values())}"



## no.3
## Which color is the median?
def median():
    sortedList = sorted(mainDictColAndVal.values())
    numItems = len(sortedList)
    if numItems % 2 == 1:
        midNum = numItems/2
        midVal = sortedList[numItems]
        return f"The median Color is = {midVal}"
    elif numItems % 2 == 0:
        midEvenNum = numItems/2
        midNum = ((midEvenNum - 1) + midEvenNum)/2
        midVal = sortedList[round(midNum)]
        for keY, vaL in mainDictColAndVal.items():
            if vaL == midVal:
                return f"The median Color is {keY}"



## no.4
## BONUS Get the variance of the colors
def variance():
    figurE = 0
    for digiT in mainDictColAndVal.values():
        meanMinusValue = abs(meanVal - digiT)
        figurE += meanMinusValue
    sqrSum = figurE ** 2
    variancE = sqrSum/count
    return f"Variance is {digiT}"



## no.5
##  BONUS if a colour is chosen at random, what is 
# the probability that the color is red?
def probRedColor():
    redColor = "RED"
    if redColor in mainDictColAndVal.keys() and redColor == "RED":
        prob = mainDictColAndVal["RED"] / totalColor
    return f"Probability of Red is {prob}"



## no.6
## Save the colours and their frequencies in postgresql database
# CREATE TABLE "colorsandfrequency" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "colors" varchar(100) NOT NULL, "frequency" varchar(100) NOT NULL);
# COMMIT;



## no.7
##  BONUS write a recursive searching algorithm to search 
# for a number entered by user in a list of numbers.
# def binary_search(arr, low, high, x):
#     if high >= low:
#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
#         else:
#             return binary_search(arr, mid + 1, high, x)
#     else:
#         return -1
    
# search = list(mainDictColAndVal.values())
# binSearch = binary_search(search, 1, 16, 6)
# print(f"binSearch list is {search}")
# print(f"binSearch is {binSearch}")



## no.8
## Write a program that generates random 4 digits number of
## 0s and 1s and convert the generated number to base 10
def randomNum():
    first = randint(0, 1)
    second = randint(0, 1)
    third = randint(0, 1)
    return f"The random number is {first}{second}{third}"



## no.9
## Write a program to sum the first 50 fibonacci sequence.
def fibonacciNumber(number):
    if number < 0:
        print("Number cannot be less than Zero")
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacciNumber(number-1) + fibonacciNumber(number-2)

# fib = fibonacciNumber(10)
# print(f"Fibonacci is {fib}")