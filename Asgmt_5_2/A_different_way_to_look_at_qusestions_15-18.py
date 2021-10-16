
# A different way to look at the question 15 -18.  Ehsan/Feb. 05, 2021/Team IV/Assignment Day 5
print("\n\033[1;31;44m A different way to look at the question 15 -18.  Ehsan/Feb. 05, 2021/Team IV/Assignment Day 5 \033[0;37;40m")
#15-FRINGE
myDic = {"Fruit":["apple", "banana", "cherry", "orange"], "Price":[5.52, 0.77, 2.54, 3.44]}                        
print("Exe.15 (Fringe)- Created myDic: ", myDic, "Type :", type(myDic))
#16-FRINGE
myDic.update({"Price":[6.44, 0.77, 2.54, 3.44]})
print("Exe.16 (Fringe)- Changed the apple price: ", myDic)
#17-FRINGE
myDic["Fruit"]=["apple", "banana", "orange"]                                                                                
myDic["Price"]=[6.44, 0.77, 3.44]                                                                                                                                              
keyList = [x3 for x3 in myDic.keys()]                                                                                                                                           
print("Exe.17 (Fringe)- a) \"cherry\" removed from myDic: ", myDic,"\n\tb) Print all keys:   ", keyList)                          
#18-FRINGE                                                                                                                                                                  
berries = {"blackberry": 1.24, "blueberry": 3.14}
myDicBr = {
    "berries":berries
}
myDic.update(myDicBr)
print("Exe.18 (Fringe)- Added \"berries\" to myDic: ", myDic)
print("\n*** End ***\n")