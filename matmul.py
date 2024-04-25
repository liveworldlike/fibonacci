def matmul(A, B):
    a, b, c, d = A
    w, x, y, z = B
    return (
        a * w + b * y,
        a * x + b * z,
        c * w + d * y,
        c * x + d * z,
    )
