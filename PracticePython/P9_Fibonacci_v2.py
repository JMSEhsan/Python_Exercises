# Ref.: Classic Computer Science Problems in Python by David Kopec, Manning, 2019
# Fibonacci recursive using memorization
# Now the Fibonacci sequence for big numbers can be calculated
# I added to the orignal code

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # base cases

def fib2(n: int) -> int:
    if n not in memo and n >= 0:
        memo[n] = fib2(n-1) + fib2(n-2)  # memorization
        return memo[n]
    elif n in memo:
        return memo[n]
    else:
        print("A negative number is not in Fibonacci sequence!")

e = True
while e == True:
    try:
        x = int(input("Enter an integer, (Press any letter to exit): "))
        if __name__ == "__main__":
            print("fib(", x+1 ,") -> ", fib2(x))
    except ValueError:
        print("Thank you!")
        e = False