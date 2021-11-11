# Ref.: Classic Computer Science Problems in Python by David Kopec, Manning, 2019
# recursive attempt
# I added to the orignal code

def fib(n: int) -> int:
    if n >=0 and n < 2:         # base case
        return n
    elif n < 0:
        print("A negative number is not in Fibonatcci series!")
    else:
        return fib(n - 2) + fib(n - 1) # recursive case

x = int(input("Enter an integer: "))
if __name__ == "__main__":
    print("fib(", x ,") -> ", fib(x))