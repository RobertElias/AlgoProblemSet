def twoNumberSum(array, targetSum):
    #for loop to iterate the array
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return[]
    print(twoNumberSum(3,2))

def twoNumSum() 