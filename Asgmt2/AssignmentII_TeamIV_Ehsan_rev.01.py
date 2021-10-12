#Assignment 2
AsmntN = input("Enter assignment number: ")   #Enter Assignmet Number
print("")
from datetime import date
today = date.today()     #Updates the date automatically every day
print("Exe.1 \033[1;34;47m Ehsan's work on assignment", "\033[1;32;47m", AsmntN, "\033[1;34;47m", "***", "Team IV", "***", "\033[1;35;47m", today, "\033[1;34;47m", "***", "Day", "\033[1;32;47m", AsmntN, "\033[1;34;47m", "Assignmet ", "\033[0;37;40m", "")
print("")
print("Exe.2")
v1 = "Ehsan"
v2 = 7
print(v1, "Likes number", str(v2),)
print("")
print("Exe.3")
mylist = ["pomegranate", "dates", "fig"]
print(v1, "likes", mylist)
print("")
print("Exe.4")
import math
Pi = math.pi
r = 5
A = int(Pi*r**2*100)/100
print("Area of a circle with radius", r, "=", A)
print("")
print("Exe.5")
z = 1 +3j
print("z =",z)
print("Type of variable =", type(z))
print("")