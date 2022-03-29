def prog_arithmetic_by_term(first, r, n):
    if n == 1:
        return first
    return first + (n - 1) * r


def prog_arithmetic(N, u, r):
    res = [u]
    for n in range(2, N + 1):
        res += [prog_arithmetic_by_term(u, r, n)]
    return res
