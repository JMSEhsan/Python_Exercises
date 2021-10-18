print("\n\t\033[1;30;47m Ehsan *** Feb. 08, 2021 *** Team IV *** Assignment Day 6 \033[0;37;40m\n")

#1
cM = 65
iG = str()
if cM > 95 and cM < 100:
    iG = "A+"
elif cM > 90 and cM < 94:
    iG = "A-"
elif cM > 85 and cM < 89:
    iG = "A"
elif cM > 80 and cM < 85:
    iG = "B+"
elif cM > 75 and cM < 79:
    iG = "B"
elif cM > 70 and cM < 74:
    iG = "B-"
elif cM > 69 and cM < 67:
    iG = "C+"
elif cM > 64 and cM < 66:
    iG = "C"
else:
    print("Entered score is out of the range")
print("Exe.1- Course Mark:", cM, "is:", iG)

#2
print("\nExe.2-")
t = -1
print("It is Freezing") if t < 0 else print("The weather is OK") if t > 0 and t < 15 else print("The weather is great")

#3
print("\nExe.3- \n")

for i in range(4):
    spcList=[" "," "," "," "," "," "," "]
    spcStr=""  
    for j in range(3-i,i+4):
          spcList[j]="*"
    for x in spcList:
        spcStr=spcStr+spcList[spcList.index(x)]
    print(spcStr)
print(" ")

#4
numList = [ 1, 7, 8, 6, 11]
sn = 0
for x in numList:
    sn = x**2 + sn
print("\nExe.4- The sum of squares of values in this list,", numList, ", =", sn)

#5
print("\nExe.5-")
numList = [ 1, 7, 8, 6, 11]

nList = list()
def sumSq_recursion(nList):
    if len(nList) == 0:
        return 0
    else:
        print("Sub-lists:", nList)
        nListmb = nList[0]
        nList.pop(0)
        result = nListmb**2 + sumSq_recursion(nList)
    return result
print("Total recursion of sum of squars:", sumSq_recursion(numList))

#6
numList = [ 1, 7, 8, 6, 11]
mList = list()
def bubble_Sort(mList): 
    n = len(mList) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if mList[j] > mList[j+1]: 
                mList[j], mList[j+1] = mList[j+1], mList[j] 
    return mList        
print("\nExe.6- Bubble-sorted", numList, "is :",bubble_Sort([1, 7, 8, 6, 11]),"\n") 