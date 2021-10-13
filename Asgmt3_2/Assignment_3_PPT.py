print("") #space
print("Assignment 3")  

Nm = input("User first name? ")
C = input("Enter current temperature in deg C: ")
print("Current teperature is ", C, "C", "***", "the input type is: ", type(C))
C = float(C)
print("")
F = C*9/5+32
print("Curent temperature in degrees Fahrenheit is:" , F, "F")
if C>21:
    print(Nm, "\033[0;31;40m, it is warm outside!", "\033[0;37;40m")
elif C<21:
    print(Nm, "\033[0;34;40m, it is cool outside!", "\033[0;37;40m")
else:
    print(Nm, "\033[0;32;40m, it is perfect outside!", "\033[0;37;40m")
    print("")

