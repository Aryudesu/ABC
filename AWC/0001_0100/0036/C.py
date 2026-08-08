def is_clear(L, K, A, S):
    c = 0
    p = 0
    for a in A:
        if a - c <= S:
            c = a
            p += 1
        if K == p:
            break
    return K == p and L - c <= S

def calc(L, K, A):
    le = -L
    ri = 0
    while le + 1 < ri:
        tmp = (le + ri) // 2
        if is_clear(L, K, A, tmp):
            le = tmp
        else:
            ri = tmp
    if is_clear(L, K, A, ri):
        return ri
    return le

N, K = [int(l) for l in input().split()]
data = [-int(l) for l in input().split()]
A = []
s = 0
for dat in data:
    s += dat
    A.append(s)
L = sum(A)
print(calc(L, K, A))
