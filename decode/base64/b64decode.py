#!/usr/bin/python
import base64

'''

This script will allow the user to decode a base64 encoded string multiple times.
    *User inputs a base64 encoded string.
    *The string is decoded by default once, or as many times as entered by the user.
    *The decoded base64 string is output as a result.

Author: r4mzih4x 

Tested on:
    Python 2.7.14

'''

# Function to decode the user base64 string multiple times
def b64dcode (userString):
    global b64converted
    b64converted = base64.b64decode(userString)

# Store the user input of a base64 encoded string
b64string = raw_input("Enter base 64 encoded string: ")

print ("\nYou entered the following string:\n " + b64string)

# Initial function call with user input
b64dcode(b64string)

# Will decode strings encoded up to 1000 times
count = 1000

# Add a counter to track the amount of attempts to decode
attempts = 0

while (count > 1):
    print ("\nNext Decoded String:\n " + b64converted)
    attempts += 1
	
    try:
	b64dcode(b64converted)
    
    except:
    # Base64 string has been fully decoded
        break
	
    count -= 1

print ("\nFinal Decoded String:\n " + b64converted)


print ("Base64 decoded text has been saved to b64decoded.txt")

# Create a text file to store the decoded base64 text
txtFile = open("b64decoded.txt", "w")
txtFile.write(b64converted)
txtFile.close()
