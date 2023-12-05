# from Question import Question
# from niceone import Students
import datetime
import calendar
import  os

#
# student1 = Students("eniola", "earth-bending", 4.0, True)
#
# print(student1.GPA)
#
# Question_prompts = [
#     "what color are you? \n(a) blue \n(b) purple \n (C) brown \n\n",
#     "what cartoon are you? \n(a) Red \n(b) green \n (C) orange \n\n",
#     "what laptop are you? \n(a) teal \n(b) purple \n (C) orangutan \n\n",
# ]
#
# questions = [
#     Question(Question_prompts[0], "a"),
#     Question(Question_prompts[1], "c"),
#     Question(Question_prompts[2], "b"),
# ]
#
#
# def Runtest(questions):
#     score = 0
#     for question in  questions:
#         answer = input(question.prompt)
#         if answer == question.Answer:
#             score = +1
#     print("you got " + str(score) + "/" + str(len(questions)) + "correct")
#
#
# Runtest(questions)
#
# aph = input("please insert an alphabet")
#
# if ( (aph == "a") |  (aph == "e")| (aph == "i") | (aph == "o")| (aph == "u") | (aph == "A")|(aph == "O")|(aph == "I")|(aph == "E")|(aph == "U")):
#     print(aph + " is a vowel")
#
# else:
#     print(aph, "is a consonant")

#First method
# a = int(input("please input a number: \t"))
# b = int(input("please input second  number: \t"))
# c = int(input("please input third number \t"))
#
# if ((a < b) & (a < c) ):
#     print(a, "is the lowest number")
# elif(b< a & b > c):
#     print(b, "is the lowest number")
# else:
#     print( c, "is the lowest number")
#
# #sheesh
# print(min(a,b,c), "is the lowest number")

# print(datetime.date.today())

# print(calendar.calendar(2022))

# password = "Koyejo"
# for a in range(3):
#     psw = input("Enter your password  ")
#     b = 2
#     if (psw == password):
#         print("Wake up to reality")
#     else:
#         print("Access denied", b-a)
# if(b - a  == 0 and psw != password):
#     myp = print("Try again")


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "not found"
        case 418:
            return "im a teapot"
        case 304 :
            return print("Something is wrong with the connection")


# http_error(304)

# adder = lambda adde : adde * 30
#
# print(adder(3))
#
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
# fib(100)

class exes:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def printname(self):
        print("{} is {} years old.".format(self.name,self.age))

class baddies(exes):
    pass

bad = baddies("Meegan", 34)
baddies.printname(bad)

class DummyClass:
    pass
Colors  = DummyClass()
Colors.alarm = "red"
Colors.AC =  "white"
Colors.wall = "green"
Colors.bed = "brown"

print("The {} alarm and {} AC is at the {} class".format(Colors.alarm,Colors.AC,Colors.wall))















