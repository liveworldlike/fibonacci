import matpow


def f(n: int) -> int:
    mat = (1, 1, 1, 0)
    _, _, res, _ = matpow.f(mat, n)
    return res
