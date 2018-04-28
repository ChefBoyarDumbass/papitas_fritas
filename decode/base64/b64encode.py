#!/usr/bin/python
import base64

'''

This script will allow the user to encode a string in base64 format multiple times.
    *User inputs a regular string.
    *The string is encoded by default once, or as many times as entered by the user.
    *The encoded base64 string is output as a result.

Author: r4mzih4x 


Tested on:
    Python 2.7.14

'''

# Function to decode the user base64 string multiple times
def b64encode (userString):
    global b64converted
    b64converted = base64.b64encode(userString)

# Store the user input of a base64 encoded string
string = raw_input("Enter a string to encode in base64: ")

# Ask the user how many times they want to encode the string
iterations = raw_input("Enter the number of times to encode the string: ")
# Add if statement to check isnumber otherwise set to 1

print ("\nYou entered the following string: " + string)
print ("\nThe string will be encoded " + iterations + " times!\n")


# Initial function call with user input
b64encode(string)

# Convert user input iterations to int for loop count
count = int(iterations)


while (count > 1):
    print ("\nNext encoded String:\n " + b64converted)
    b64encode(b64converted)
    count -= 1


print ("\nFinal Encoded String:\n " + b64converted)
print ("Base64 encoded text has been saved to b64encoded.txt")

# Create a text file to store the encoded base64 text
txtFile = open("b64encoded.txt", "w")
txtFile.write(b64converted)
txtFile.close()
