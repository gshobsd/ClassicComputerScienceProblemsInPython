# file calculates pi using Leibniz's formula
from timeit import default_timer as timer

def calculate_pi(n_terms: int) -> float:
    start: float = timer()
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    end: float = timer()
    return (end - start, pi)


def calculate_pi2(n: int) -> float:
    start: float = timer()
    pi: float = 0.0
    denominator: int = 1
    sign: int = 1
    for _ in range(n):
        pi += sign * 4 / denominator
        denominator += 2
        sign = -sign
    end: float = timer()
    return (end - start, pi)

if __name__ == "__main__":
    for i in range(7,8):
        rt1, p1 = calculate_pi(10 ** i)
        rt2, p2 = calculate_pi2(10 ** i )
        if rt1 < rt2:
            print("calculate_pi faster than calculate_pi2")
        else:
            print("calculate_pi2 faster than calculate_pi")
        print("\tcp: {}, cp2: {}, pis are equal: {}".format(rt1, rt2, p1 == p2))