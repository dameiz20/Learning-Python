#Variables

name = "dakota"
age = 21

#EXPRESSIONS AND STATEMENTS

#statement <-- a program is formed by a series of statements. they can be placed on two seperate lines or they can be placed on the same line with a ; seperating them
name = "dakota"
print(name)

#DATA TYPES
# you can do a type() if you wwant to know what type of data type a peice of code is

#int = 2 <-- any whole number is an int
#float = 2.9 <-- any number can be a float but all numbers with decimal points are always floats
#string any block of code that is in double quotes " this is a string " 
# you can also do what is called casting to make a number a string, for example
#number = "20"
#age = int(number)
#print(isinstance(age, int))

#common types of types
#complex for complex numbers
#bool for booliean
#list for lists
#tuple for tuples
#range for ranges
#dict for dictionaries
#set for sets


#OPERATORS

##Arithmetic Operators

#1  1 + 1 plus ( the plus can also be used for concatination of string)
#2  1 - 1 minus (the minus can be used to make a negative number for example 2 + -2)
#3  2 * 2 multiply
#4  4 / 2  divide
#5  4 % 3 remainder
#6  4 ** 2 exponents
#7  4 // 2 floor division ( does division and rounds down to nearest whole number)

# toy can also use any operator combined with an = for ease of code for example
#age = 8
#age += 8 # this means age = age + 8  so esentialy what we are saying is age == 8(age) + 8 (the 8 from the problem) so 8 +8 = 16
#print(age) <-- this should print out 16 because of ^^

##Comparison Operators
#a == b equals
#a != b not equalls
# a > b greater than 
# a <= b less than or equal to 

## ^^^^^ These will all  give a true or false values or whats known as a boolean value

##Boolean Operators

condition1= True
condition2 = False

not condition1 # false 
condition1 and condition2 # false
condition1 or condition2 #true




#variables name can be composed of characters numbers and underscore character but cannot start with a number
#for example
#name1
#HEIGHT
#my_name
#__name__

#invalid varable names
#123
#test!
#test%
# or python key words such as 
#for, if, while, import