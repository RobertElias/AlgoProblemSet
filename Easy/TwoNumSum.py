array = [3,5,-4,8,11,-1,6]
targetSum = 10
def twoNumberSum(array, targetSum):
    #for loop to iterate the array
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return[]
#    print(twoNumberSum(firstNum, secondNum))

# Second Solution
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# Third Solution
def TwoNumSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range( i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []