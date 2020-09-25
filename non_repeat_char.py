
  
# Returns an array of size 256 containg count 
# of characters in the passed char array 
# def getCharCountArray(string): 
#     count = [0] * NO_OF_CHARS 
#     for i in string: 
#         count[ord(i)]+= 1
#     return count
    
def first_not_repeating_character(string):
   
    res = "_"
    d = {}
    for i, c in enumerate(string):
        if c in d.keys():
            d[c]= -1
        else:
            d[c] = i
    min_key = len(string) + 1
    for k in d.keys():
        if d[k]>=0:
            min_key = min(min_key,d[k])
            res = string[min_key]
    return res