class Solution:
    # data structure type: stack
    def decodeString(self, s: str):
        #Traverse the string
        stack, currCount, currString = [], 0, ""
        for c in s:
            if c == '[':
                stack.append(currString)
                stack.append(currCount)
                currString = ""
                currCount = 0
            elif c == ']':
                count = stack.pop()
                prevStr = stack.pop()
                currString = prevStr + currString * count
                        
            elif c.isdigit():
                currCount = currCount * 10 + int(c)

            else: # character 
                currString += c

        return currString