def encrypt(text,s):
    result = ""
    #traverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        # Encrypt lowercase characters in plain text    
        return result
#check the above function    
text = "CEASERCIPHERDEMO"
s = 4

print("Plain Text: " + text)
print("Shift pattern: " + str(s))
print("Cipher: " + encrypt(text,s))
