N, Q = map(int, input().split())
C = list(map(int, input().split()))
data = []
prev = -1
for c in C:
    if c != prev:
        data.append(1)
    else:
        data.append(0)
    prev = c
print(data)
for _ in range(Q):
    n, *query = list(map(int, input().split()))
    if n == 1:
        l, r, x = query
    elif n == 2:
        l, r = query
    else:
        raise ValueError()
# 終わります！！！
