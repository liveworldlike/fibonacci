import matmul


def f(A, p):
    res = (1, 0, 0, 1)
    while p:
        if p & 1:
            res = matmul.f(res, A)
        A = matmul.f(A, A)
        p >>= 1
    return res
