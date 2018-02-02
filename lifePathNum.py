month = int(input("Please enter your month of birth (1~12): \n"))
day = int(input("Please enter your day of birth (1~31): \n"))
year = int(input("Please enter you year of birth(YYYY): \n"))


#Calculate month of birth between 1 to 9
def calNum(numbers):
    total = 0
    while numbers > 0:
        num = numbers % 10
        total += num
        numbers //= 10
    if total >= 10:
        total = calNum(total)
    return total

#To find a life path
def checkOneNum(largeNum):
    result = 0
    #If the life path is 11, result should be 11
    if largeNum == 11:
        result = largeNum
    #IF the life path is 22, result should be 22
    elif largeNum == 22:
        result = largeNum
    #If the life path is less than 10, the number stores in result
    elif largeNum < 10:
        result = largeNum
    #If the life path is equal and larger than 10, calculate fewer than 10
    else:
        largeNum = calNum(largeNum)
        if largeNum >= 10:
            largeNum = calNum(largeNum)
        result = largeNum
    return result

month = calNum(month)
day = calNum(day)
year = calNum(year)
#To add all of them
total = month + day + year
#To find a life path
lifePath = checkOneNum(total)
print ("Your life path is" , lifePath)
