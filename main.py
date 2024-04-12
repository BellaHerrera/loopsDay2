# #order of execution
# # in python 

# print("hello world")
# #stings are surrounded by quotes
# # single or double quotes "" or ''
# # be consistent with the quotes you use
# print("order of execution")
# print("in python")
# print("*"*20)

# #variables are used to store data
# #variables are created when you assign a value to it
# #variables are case sensetive
# price = 10 #integer variable 
# name = "John" #string variable
# rating = 4.9 #float variable
# is_published = True #boolean variable
# #start all variables with a lower case letter or underscore
# #use underscores to separate words (_)
# #use camel case if you want to start with a capital letter 
# #on the next word
# playBulls = "michael jordan" 

# #concatenation to join variables
# print(name +  " is a basketball player")
# print(name + " has a rating of" + str(rating))
# #use the str() function to convert a number to a string
# #the plus sign (+) is used to concatenate strings
# print("the price of the book is" +str(price))

# #getting input fromt the user
# name = input("what is your name?")
# age = input("what is your age?")
# print("hello" + name + "you are" + age + "years old")

#ask 2 question from the user
#persons name and favorite color
#then print a message like "moses like blue"

name = input("what's your name?")
favorite_color = input("what is your favorite color?")
print("hello" + name + "likes" + favorite_color)