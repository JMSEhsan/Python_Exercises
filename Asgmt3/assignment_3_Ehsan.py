#Assignment 3
AsmntN = input("Enter assignment number: ")   #Enter Assignmet Number
print("")
from datetime import date
today = date.today()     #Updates the date automatically every day
print("\033[1;34;47m  Ehsan's work on assignment", "\033[1;32;47m", AsmntN, "\033[1;34;47m", "***", "Team IV", "***", "\033[1;35;47m", today, "\033[1;34;47m", "***", "Assignmet Day", "\033[1;32;47m", AsmntN, " \033[0;37;40m")
print("")
print("Exe. 1:")
myFruits = ("Apple", "Peach", "Banana")
print("myFruits :", myFruits, "    Type: ", type(myFruits))
print("")
print("Exe. 2:")
MyFtList = list(myFruits)                                                         # MyFtList = [] together with MyFtList.extend(myFruits)  will do too
print("myFruits converted to a list:", MyFtList, "    Type: ", type(MyFtList))        
print("")
print("Exe. 3:")
import random
RAN = random.randrange(100,200)
print("A random number between 100 and 200: ", RAN)
print("")
print("Exe. 4:")
myCat = "The gray cat is under the bed, is it?"
print("sub string: ", myCat[4:12])
print("")
print("Exe. 5:")
if "dog" in myCat:
    print("The word \"dog\" is in myCat")
else:
    print("The word \"dog\" in NOT in myCat")
print("")
print("Exe. 6:")
print(myCat[-6:])
print("")
print("Exe. 7:")
print(myCat.replace("cat", "dog"))
print("")
print("Exe. 8:")
mCs = myCat.split(",")
(a, b) = mCs
print("Split myCat using \",\" :", mCs)
print("Printing the two strings:", "\n", a, "\n", b.strip())
print("")
print("Exe. 9:")
vp = 5.5
svq = 5
txt = "We bought {1} peaches for {0:0.2f} $"
print(txt.format(vp, svq))
print("")
