print("\n","\bEhsan  ***  Feb. 04, 2021 *** Team IV *** Assignment Day 4 \n")

#1  
print("Exe.1- Division remainder of 7 over 5 = ", 7 % 5)

#2
if 7 >= 5:
    print("Exe.2- Checked, 7 is greater than or equal to 5")
else:
    print("Exe.2- Checked, 7 is NOT greater than or equal to 5")

#3
print("Exe.3- Binary Shift \"4\" by \"2\" = ", 4<<2, " decimal (base 10)")        # 10000 in binary (base 2)

#4
myList = []
addList = ["apple", "banana", "cherry", "apple", "cherry"]
myList.extend(addList)
print("Exe.4- a) myList: ", myList)
ci = myList.index("cherry")
ai = myList.index("apple")
print("\t\bb) \"",myList[ci],"\"", ",", "\"",myList[ai],"\"")

#5
print("Exe.5- Lenth of myLsit: ", len(myList))

#6
print("Exe.6- Last two items on myList: ", myList[-2],",", myList[-1] )

#7
for x in myList:
        if x == "apple":
            ai = myList.index("apple")
            myList[ai:ai+1] = ["grapes", "papaya"]

print("Exe.7- Changing the apple with grapes and papays: ", myList)

#8
myList.append("grapes")                                                            #2nd method:  #myList.insert(len(myList), "grapes")  
print("Exe.8- Appending grapes at the end: ", myList)                                                                  

#9                              
if "papaya" in myList:                                                             #2nd method of removing "papaya":    for y in myList:                                     
    print("Exe.9- a) Checked, papaya is on myList")                                                                           #if y == "papaya":
    mynewList = [y for y in myList if y != "papaya"]                                                                                #myList.remove("papaya") 
    print("\t\bb) papaya removed: ", mynewList)                                                                                
else:
    print("Exe.9- Checked, papaya is NOT on myList")                                                                                                                                                                                                     
 
#10
mynewList2 = [M.upper() for M in mynewList]
print("Exe.10- myList in uppercase: ", mynewList2)

#11
mynewList2.sort(reverse = True)
print("Exe.11- Sorting the list descending: ", mynewList2)

print("\n*** End ***\n")