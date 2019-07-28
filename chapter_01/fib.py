from typing import Dict #required for fib3

# the fib1 code is broken by design in the book.
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

# fib2 does define a base case, but for for all intents and purposes
# is broken, in terms of efficiency. 
# I've added some debug prints to demonstrate the design failures.
def fib2(n: int, s: int = 2) -> int:

    if s == 0:
        side = "left"
    elif s == 1:
        side = "right"
    else:
        side = "initial call"
    print("fib2() called with n = {}. Side = {}".format(n, side))
    if n < 2: 
        return n
    return fib2(n - 2, 0) + fib2(n - 1, 1)


# this is saving state as we going along, thus not having
# not having to perform calculations a second time.
memo: Dict[int, int] = {0: 0, 1: 1}     # our base case
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # memoization
    return memo[n]


# the functools library allows automatic memoziation with
# the lru_cache decorator. This should be about as fast
# as fib3().
from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    print("fib4(): {}".format(n))
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)

# using an iterative method (my favorite and
# the fastest).
def fib5(n: int) -> int:
    if n == 0:
        print("Base case: 0")
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        print("fib5(): next = {}, last = {}".format(next, last))
        last, next = next, last + next  # cute.
    return next


# lastly (from the book) building a generator.
from typing import Generator
def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == "__main__":
    #  Running fib1 will cause a Recursion Error due to the
    # lack of a base case.
    # print(fib1(5))

    print(fib2(5))