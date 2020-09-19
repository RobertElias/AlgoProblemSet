
# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome. A palindrome is defined as a string
# that is written  the same forward and backward. Note that single char strings are palindromes.

# # Solution #1
# # O(n^2) time | O(n) space

# def isPalindrome(string):
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

# Solution #2
# O(n) time | O(n) space

# def isPalindrome(string):
#     #store in array
#     reversedChar = []
#     for i in reversed(range(len(string))):
#         reversedChar.append(string[i])
#     return string == reversedChar

# Solution #3
# O(n) time | O(n) space

def isPalindrome(string, i = 0):
    #store in array
    stored = len(string) - 1 - i
    return True if i >= stored else string[i] == string[stored] and isPalindrome(string, i + 1)
    pass