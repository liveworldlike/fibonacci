from matmul import matmul


def matpow(A, p):
    res = (1, 0, 0, 1)
    while p:
        if p & 1:
            res = matmul(res, A)
        A = matmul(A, A)
        p >>= 1
    return res
