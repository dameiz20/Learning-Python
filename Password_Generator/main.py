# importing the random integer module from the random library
import random
from random import randint
import string

# password that will work with  most pasword compliances
password = " "
for i in range(1):
    i = chr(randint(65, 90)) 
    password = str(password)+ i # setting uppercase letter to display once and setting that leter to password
    for x in range (9):
        x=chr(randint(65,90)).lower()
        password = str(password) + x # taking the new password that was just set to the single uppercase digit and adding the 9 lowercase digits to it 
    password = password + random.choice(string.punctuation)# adding a random special character to the end of the password to meet most password requirements
print(password) # printing out the new password with both the uppercase and lowercase sections combined.



