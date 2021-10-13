
print("\n\t\033[1;30;47m Ehsan *** Feb. 05, 2021 *** Team IV *** Assignment Day 5 \033[0;37;40m\n")

#1
Tuple1 = ("apple",)
print("Exe.1- Print created tuple and type: ", Tuple1, "    Type: ", type(Tuple1))
#2
myTuple = ("apple", "banana", "apple", "cherry", "orange", "kiwi", "melon", "mango")
print("Exe.2- a) myTuple =", myTuple, "\n\t\bb) Print \"orange\" or \"kiwi\" if found in myTuple: ")
omList = ["orange", "kiwi"]                                                                                       # General solution for repeating items 
riList = list()
for x1 in omList:
    for i in range(len(myTuple)):
        if myTuple[i] == x1:
            riList.append(i)                                 # Adds multiple index numbers of the item to the list. For repeated items and general purpose
            iLoop3 = myTuple[i]
    txt = "\t  {:<10}   Number of times \"{:^6}\" has been repeated: {:<4}     Index: {}"
    print(txt.format(iLoop3, x1, myTuple.count(myTuple[i]), riList))
    riList.clear()
#3                                                                                                                
j = 0
for x2 in myTuple:
    if x2 == "MANGO":
        print("Exe.3- ", x2, "is in the list")
    elif x2 == "mango":
        txt = "Exe.3- \033[1;31;43m\"MANGO\"\033[1;31;40m is NOT in the list\033[0;37;40m; (but \033[0;30;42m\"{}\"\033[0;37;40m is in the List)"
        print(txt.format(x2))
    else:
        if j == len(myTuple)-1:                                       # Only prints once if there is no "MANGO" in the list
            print("Exe.3- \"MANGO\" is NOT in the list")
        j = j + 1
#4 
myList = list(myTuple)
myList.append("papaya")
myTupleUPD = tuple(myList)
print("Exe.4- Add papaya to myTuple: ", myTupleUPD, "    Type: ", type(myTupleUPD) )
#5  
myNewTuple = myTupleUPD[-3:]                                                                                                # Method 2- (*fver, ver3, ver2, ver1) = myTupleUPD
print("Exe.5- myNewTuple created: ", myNewTuple, "    Type: ", type(myNewTuple))                                                        #myNewTuple = (ver3, ver2, ver1)
#6
(var1, var2, var3) = myNewTuple
(x, y, z) = (var1, var2, var3)
print("Exe.6- Variable 1:    x =", x, "     Type:" , type(x), "\n\t\bVariable 2:    y =", y, "     Type:" , type(y), "\n\t\bVariable 3:    z =", z, "    Type:", type(z))
#7
TupleTA = ("Watermelon", "Guava")
myNewTuple2 = myNewTuple + TupleTA
print("Exe.7- myNewTuple:", myNewTuple2, "     Type: ", type(myNewTuple2)) 
8#
IK = myTupleUPD.index("kiwi")
print("Exe.8- kiwi index: ", IK)
#9
mySet = set(myTupleUPD)
print("Exe.9- Created mySet from myTuple:", mySet, "    Type:", type(mySet), "    Length:", len(mySet))
#10:
mySet.add("orange")
print("Exe.10- \"orange\" added to mySet: ", mySet, "    Length:", len(mySet))
#11
mySet.update({"pineapple", "mango"})
print("Exe.11- {\"pineapple\", \"mango\"} added to mySet: ", mySet, "Length: ", len(mySet))
#12
mySet.discard("Watermelon")
print("Exe.12- Tried to remove \"Watermelon\" form mySet: ", mySet)
#13
mySetUP = {m.upper() for m in mySet}
print("Exe.13- Printed all the set items in upper case: ", mySetUP)
#14
setGiven = {"apple", "cherry", "orange"}
mySetUPD2 = mySet.intersection(setGiven)
print("Exe.14- Common elements: ", mySetUPD2)
#15
myDic = {"apple":5.52, "banana":0.77, "cherry":2.54, "orange":3.44}                          # There may be a different way to look at the question 15 -18. (code comes in a separate file)                    
print("Exe.15- Created myDic: ", myDic, "     Type :", type(myDic))
#16
myDic["apple"] = 6.44
print("Exe.16- Changed the apple price: ", myDic)
#17
myDic.pop("cherry")                                                                                                   # Method 2- Print all keys separatly: for x in myDic.keys():
keyList = [x3 for x3 in myDic.keys()]                                                                                                                                # print(x)
print("Exe.17- a) \"cherry\" removed from myDic: ", myDic,"\n\tb) Print all keys:   ", keyList)                       # Method 3- Print all keys in a list with the label, "dict_keys" : print("All keys: ", myDic.keys())
#18                                                                                                                                                                   
berries = {"blackberry": 1.24, "blueberry": 3.14}
myDicBr = {
    "berries":berries
}
myDic.update(myDicBr)
print("Exe.18- Added \"berries\" to myDic: ", myDic)
print("\n*** End ***\n")