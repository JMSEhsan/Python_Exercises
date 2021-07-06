#6 Practice

[m1, m2, m3, m4, m5, m6, m7] =[int(),int(),int(),int(),int(),int(),int()]
spcList = [m1, m2, m3, m4, m5, m6, m7]
for i in range(4):
    for x in spcList:
        x = 32
    for j in range(3-1,i+4):
        spcList[j] = 42
        print(spcList)
    [m1, m2, m3, m4, m5, m6, m7] = spcList
    txt = "{:c}{:c}{:c}{:c}{:c}{:c}{:c}"
    print(txt.format(m1, m2, m3, m4, m5, m6, m7))  
        