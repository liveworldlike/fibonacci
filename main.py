import argparse
import sys
from fib import fib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('--max-digits', type=int, default=1000)
    args = parser.parse_args()
    sys.set_int_max_str_digits(args.max_digits)
    print(fib(args.n))
