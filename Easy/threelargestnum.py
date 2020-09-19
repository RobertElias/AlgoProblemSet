#Write a function that takes in an array of at least three integers
# and without sorting the input array, returns a sorted array
# of the three largest integers in the input array.
# The function should return duplicate integers if necessary; for example, 
# it should return [10,10,12]for inquiry of [10,5,9,10,12].

#Solution 1
# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    # Write your code here.
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

# method helper function
def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

# method helper function
def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            arrya[i] = array[i + 1]
    pass