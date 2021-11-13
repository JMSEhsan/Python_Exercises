# Ref.: Classic Computer Science Problems in Python by David Kopec, Manning, 2019
# Fibonacci recursive - automatic memorization
# The Fibonacci sequence for bigger numbers can be calculated
# I added to the orignal code

from functools import lru_cache   # Python built-in decorator for memorizing any function automagically

@lru_cache(maxsize = None)

def fib3(n: int) -> int:    # same definition as fib1()
    if n >= 0 and n < 2:  # base case
        return n
    elif n < 0:
        print("A negative number is not in Fibonacci sequence!")
    else:
        return fib3(n - 2) + fib3(n - 1) # recursive case

e = True
while e == True:
    try:
        x = int(input("Enter an integer, (Press any letter to exit): "))
        if __name__ == "__main__":
            print("fib(", x+1 ,") -> ", fib3(x))
    except ValueError:
        print("Thank you!")
        e = False