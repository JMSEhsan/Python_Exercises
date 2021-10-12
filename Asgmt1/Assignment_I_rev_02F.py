
from printcharacters import prntspacer, prntquotmrk  # Import functions prntspacer & prntquotmrk

print(' Assignment I')
print(' Exe. 1')
import math
Pi=math.pi
print("", 'Volume of a sphere with a radius 5 = ')
print("", 4/3*Pi*5**3)
 
prntspacer()   # Called imported function
prntquotmrk()  # Called imported function

print(' Exe. 2')
print(' Total wholesale cost for 60 copies in $')
print("", 24.95*0.6*60+(3+0.75*59))

prntspacer()   # Called imported function
prntquotmrk()  # Called imported function

print(' Exe. 3')
print(' The time you get home for breakfast = ')
import datetime
a=(2*8.25+3*7.2)/60
t= 6+52/60+a
h = int(t)
m = (t*60) % 60
s = (t*3600) % 60

print("", "%02d:%02d:%02d" % (h, m, s))

prntspacer()   # Called imported function
prntquotmrk()  # Called imported function

print(' End')