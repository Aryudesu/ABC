N, XA, YA, R = map(int, input().split())
result = 0
for n in range(N):
    X, Y, P = map(int, input().split())
    if (XA-X) ** 2 + (YA-Y) ** 2 <= R**2:
        result += P
print(result)
