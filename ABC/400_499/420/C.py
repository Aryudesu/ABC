N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
result = 0
for n in range(N):
    result += min(A[n], B[n])
res = []
for q in range(Q):
    c, x, v = input().split()
    x, v = int(x) - 1, int(v)
    result -= min(A[x], B[x])
    if c == "A":
        A[x] = v
    else:
        B[x] = v
    result += min(A[x], B[x])
    res.append(result)
for r in res:
    print(r)
