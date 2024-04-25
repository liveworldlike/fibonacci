from matpow import matpow


def fib(n: int) -> int:
    mat = (1, 1, 1, 0)
    _, _, res, _ = matpow(mat, n)
    return res
