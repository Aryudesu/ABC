from atcoder.fenwicktree import FenwickTree

N, Q = [int(l) for l in input().split()]
S = input()
id = False
a = []
fw = FenwickTree(N - 1)
for idx in range(N - 1):
    if S[idx] == S[idx + 1]:
        fw.add(idx, 0)
        a.append(0)
    else:
        fw.add(idx, 1)
        a.append(1)
for _ in range(Q):
    n, L, R = [int(l) for l in input().split()]
    L -= 1
    R -= 1
    if n == 1:
        if L != 0:
            tmp = 1 - 2 * a[L-1]
            fw.add(L-1, tmp)
            a[L-1] = 1 - a[L-1]
        if R != N - 1:
            tmp = 1 - 2 * a[R]
            fw.add(R, tmp)
            a[R] = 1 - a[R]
    else:
        tmp = fw.sum(L, R)
        print("Yes" if tmp == R - L else "No")
