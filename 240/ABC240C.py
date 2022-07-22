N, X = [int(l) for l in input().split()]
res = 1
for n in range(N):
    a, b = [int(l) for l in input().split()]
    res = (res << a) | (res << b)
print("Yes" if ((res >> X) & 1) else "No")
