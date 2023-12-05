import time

# name = "joe"
# age = "45"
# print("his name is ",  name,  "and he's age is somehow "  , age)
# a = "4"
# b = "2"
# print ( int(a) + int (b) )
# name  = input("what is your name...?")
# print(name)
# print("Welcome here", name)
# print(67%3)
# x = 4;
# y= 78
# z = 23
# print(x+y*z/y)

# age = 765
#
# if  (age == 5  & age >80) :
#    print("you are not eligibe to take alcohol")
# elif (age > 20 ): print("nice you dey above 18")
# elif (age == 16): print("abeg get out")
# else:  print("you are not eligible s

# i = 0
# while (i <=  100):
#             print(i)
#             if(i ==7 ):
#                 break
#             i = i + 1
#
# grade =  {"koyejo": 34, "oluleke": 45, "propangada": 12 }
#
#
# print(grade["koyejo"])
# grade["ejike"] = 120
# print(grade)
# del grade["oluleke"]
# print(grade)
#
# def saade(sade,age):
#     print("hello " + sade, "you are " + age)
#
# saade("kike","23")
#
# def cube(num):
#     return  2*num*3
#
# print(cube(3))
#
# is_male = False
# is_tall = False
# if is_male or is_tall:
#     print("omooo")
# else:
#     print("abeg getat")

# def userinput():
#     user = input("what's the username\n")
#     print(user)
#
# print(userinput())

# print(time.time())
# print(time.localtime(1664133784.5181177))
# print(time.asctime())
#
# num = int(input("please, insert any numbers"))

# salary = input("please enter your salary \t")
# bonus = input("please enter your bonus \t")
#
# paycheck = float(salary) +float(bonus)

# print(paycheck)


# tuples
#
# coordinates = (4, 5)
# print(coordinates[0])

#functions
#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(300, 40, 53))



# num1 = float(input("what number...? \t"))
# op = (input("what operator...? "))
# num3 = float(input("enter second number...? \t"))
#
# if op == "+":
#     print(num1 + num3)
# elif op == "-":
#     print(num1 - num3)
# elif op == "/":
#     print(num1 / num3)
# elif op == "*":
#     print(num1 * num3)
# else:
#     print("Invalid statement")


#dictionary
# month_conversions = {
#     "jan": "January",
#     "Feb": "February",
#     "mar": "march",
#     "apr": "april",
#     "may": "May",
#     "june": "June",
#     "july": "july"
# }

#
# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1

# print(month_conversions.get("apr"))

#Guessing games
# secret_word = "Giraffe"
# guess = ""
# guess_number = 0
# guess_limit = 4
# out_of_guesses = False
#
# while guess != secret_word and not (out_of_guesses):
#     if guess_number < guess_limit:
#         guess = input("enter your guess: ")
#     guess_number += 1
# else: out_of_guesses = True
#
# if out_of_guesses:
#     print("You Lose")
# else:
#     print("you win!")



#for loops

# def Translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower()  in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#         else:
#             translation = translation + "g"
#         else:
#         translation = translation + letter
#     return translation
#
# print(Translate(input("Enter a phrase")))

#print("Comments are Fun")




#
# try:
#         value = 10/0
#         number = int(input("Gimme A number"))
#         print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Your Value is Not much")
#
# the_bad_File = open("index.html", "w")
#
# the_bad_File.write("<p>I am the one in this place  </p>")
#
#
# the_bad_File.close()



#
# class Students:
#
#     def __init__(self, name, course, GPA, suspensionstatus):
#         self.name = name
#         self.course = course
#         self.GPA = GPA
#         # self.suspensionstatus = suspensionstatus

weight = input("weight...? ")
measure = input('lbs or kg...?')
if weight == int():
    measure
else: measure == float()

if measure == 'l' or 'L':
   weight = weight.isdigit()
   weight*3
print(weight)
elif measure == 'k' or 'K':
    weight = weight / 2
    print(weight)
else: 'error on the weight system'



