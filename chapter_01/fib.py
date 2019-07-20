# the fib1 code is broken by design in the book.

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)




if __name__ == "__main__":
    #  Running fib1 will cause a Recursion Error due to the
    # lack of a base case.
    # print(fib1(5))