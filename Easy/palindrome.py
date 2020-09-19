
# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome. A palindrome is defined as a string
# that is written  the same forward and backward. Note that single char strings are palindromes.

# Solution #1
# O(n^2) time | O(n) space

def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString