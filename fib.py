#!python3
import argparse
from functools import cache
import sys

RECURSION_LIMIT = 12_000


def ReasonableInteger(x: int) -> int:
    x = int(x)
    if x > RECURSION_LIMIT:
        raise ValueError(f'{x} is too big!')
    return x


@cache
def fib(n: int) -> int:
    if n < 0:
        if n % 2 == 1:
            return fib(-n)
        else:
            return -fib(-n)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    sys.setrecursionlimit(RECURSION_LIMIT)
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=ReasonableInteger)
    args = parser.parse_args()
    print(fib(args.n))
