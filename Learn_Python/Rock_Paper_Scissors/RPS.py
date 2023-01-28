import random

#learing variables and functions

#creeating a function (get_choices) and assigning it our variables (player_choice and computer_choice)
def get_choices():
    # creating a variable (player_choice) and asigning it the value of rock
    player_choice = input("Enter a choice... Rock, Paper, or Scissors: ") 

    # creation a list (options) with our rock paper scissors choices
    options = ["Rock", "Paper", "Scissors"]

    #creating a variable (computer_choice) and asigning it the value of paper
    computer_choice = random.choice(options)

    # crating a dict with our choices 
    choices = {"player": player_choice, "computer" : computer_choice}
    return choices

def checkWin(player, computer):
    print(f"You chose {player}, and the computer chose {computer}")
    if player == computer:
        return "Its a tie!"
    elif player == "rock" :
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock. You Loose!"
    elif player == "paper" :
        if computer == "rock":
            return "Paper covers rock. You win!"
        else:
            return "Scissors cut paper. You Loose!" 
    elif player == "scissors" :
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You Loose!"

choices = get_choices()
result = checkWin(choices["player"], choices["computer"])
print(result)




#choices = get_choices()    
#print(choices)


 #learning dictionaries

#dicts use keys and values like shown below 
# the keys are  "name" and "color"
# the values are  "Dakota" and "blue"
# you can use variables as your values, when doing that the variable is no longer surrounded in " ".
# dict = {"name": "Dakota", "color": "blue"}




#calling functions and printing to terminal
#def greeting():
 #   return "Hello world!!!"

#greeting()
# puttinig function into variable
#response = greeting()
# thew print function prints to terminal 
#print(response)

# Getting User input
# input("plcae question you whant answered here")

#importing libraries, Creating lists, and calling methods

#importing random library
# import random

#creating list
# food = ["pizza", "Carrots", "eggs" ]

#creating a list and using the random library
#  dinner = random.choice(food) <--- we are passing in the food list from above and the random.choice method will make a random selection of the options in the food list

#creating arguments

#creating if statements
#a=3
#b=5
# if a==b: <-- make sure to use == to set something equal to or to check if something equals something else as the = by itself is the set function
# print("yes")


#concatinating Strings
#Print(" you chose " + player + ", computer chose " + computer)

#fstrings
# age = 25
#print(f"jim is {age} years old." )

#else and elif statements
#age = 20
#if age >=18:
#   print("you are an adult")
#elif age >12:
#   print (" you are a Teenager.")
#elif age > 1:
#   print("you are a child.")
#else:
#   print("you are a baby.")

# Refactoring and Nested if statment

# Accessing Dictionary Values
#choices = {"player": "Rock", "computer": "paper"}
#p_choice = choices["player"]<-- the reason we do p_choice is because we want the player choice 
#
#