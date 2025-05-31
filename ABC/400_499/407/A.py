def calc(A, B):
    if B == 1:
        return A
    if A % B == 0:
        return A // B
    tmp = A // B
    tmp2 = A % B
    tmp3 = 1 if 2 * tmp2 > B else 0
    return tmp + tmp3

A, B = [int(l) for l in input().split()]
print(calc(A, B))
