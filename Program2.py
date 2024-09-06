# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
name = input("What is your name?")
print("Hi there, " + name)


# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
print("Hi, ")
print(name)
print("!")
print(name + " is quite a nice name!")
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
#
print("Hi " + name + "! Let me make sure; your name is " + name + "?")
x=7
print (x + x + x + x)
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
newName = input("TELL ME YOUR NAME!!!!")
email = input("QUICK TELL ME YOUR EMAIL")
nickname = input("Do you have a cool nickname?? ")
print("Let me run it back")
print("Your name is " + newName)
print("Your email is " + email)
print("Your nickname is " + nickname + ". That is pretty cool.")
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)
goodcandy = input("What is your favorite candy? ")
print(goodcandy)
badcandy = input("What is your least favorite candy? ")
print(badcandy)


## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
probonename = input("What is your name?")
print(probonename)
print(probonename)

## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
probtwoname = input("What is your name?")
print( "!" + probtwoname + "!" + probtwoname + "!" + probtwoname + "!")

## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
oneName = input("What is your first name?")
lastName = input("What is your last name?")
streetAddress = input("What is your street address?")
city = input("What is your city and postal code?")
print("First name: " + oneName)
print("Last name: " + lastName)
print("Street address: " + streetAddress)
print("City and postal code: " + city)

## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
wordone = input("Give me one word")
wordtwo = input("Give me another word")
wordthree = input("Give me one last word")
print(wordone, "-", wordtwo, "-" ,wordthree)

## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.
knightname = input("Please type in a name:")
year = input("please type in a year:")
print(knightname, "is a valiant knight, born in the year", year, ".")
print("One morning ",knightname, "woke up to an awful racket: a dragon was approaching the village.") 
print("Only",knightname, "could save the village's residents.")