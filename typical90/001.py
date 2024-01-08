def is_clear(L, K, A, S):
    c = 0
    p = 0
    for a in A:
        if a - c >= S:
            c = a
            p += 1
        if K == p:
            break
    return K == p and L - c >= S

def calc(L, K, A):
    le = 0
    ri = L
    while le + 1 < ri:
        tmp = (le + ri) // 2
        if is_clear(L, K, A, tmp):
            le = tmp
        else:
            ri = tmp
    if is_clear(L, K, A, ri):
        return ri
    return le

N, L = [int(l) for l in input().split()]
K = int(input())
A = [int(l) for l in input().split()]
print(calc(L, K, A))
