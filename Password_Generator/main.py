# importing the random integer module from the random library
import random
from random import randint
import string


#All Uppercase Password
password = " "
for i in range(10):
    # setting our character to a random integer between 65 and 90 and setting it equal to i
    i = chr(randint(65, 90)) # since all letters are numbers (binary) the 65-90 are A-Z capitalized 
    password = str(password)+ i # take original password set it equal to a string and add the random letter (i) onto it and it will repeat 10x
print(password)

#All lowercase Password
#password = " "
#for i in range(10):
    # setting our character to a random integer between 65 and 90 and setting it equal to i
   # i = chr(randint(65, 90)).lower() # since all letters are numbers (binary) the 65-90 are A-Z capitalized 
   # password = str(password)+ i # take original password set it equal to a string and add the random letter (i) onto it and it will repeat 10x
#print(password)

#Upper and lowercase Alternating password
password =" "
for i in range(5):
    i = chr(randint(65,90)) # this setting the uppercase characters in the range of 5
    for j in range(5):
        j = chr(randint(65,90)).lower() # this is setting the lower case  characters in range of 5
    password = str(password) + i + j  # this is combining the upper case and lowercase character together in alternating fasion to create a total of a 10 char password
print(password)  # print out password


# normal password
password = " "
for i in range(1):
    i = chr(randint(65, 90)) 
    password = str(password)+ i # setting uppercase letter to display once and setting that leter to password
    for x in range (9):
        x=chr(randint(65,90)).lower()
        password = str(password) + x # taking the new password that was just set to the single uppercase digit and adding the 9 lowercase digits to it 
    password = password + random.choice(string.punctuation)# adding a random special character to the end of the password to meet most password requirements
print(password) # printing out the new password with both the uppercase and lowercase sections combined.



