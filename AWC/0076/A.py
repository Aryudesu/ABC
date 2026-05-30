S, P, R = map(int, input().split())
M = int(input())
result = S
for m in range(M):
    e, v = map(int, input().split())
    if e == 1:
        result += v
    elif e == 2:
        result -= v * P
    else:
        raise ValueError()
print(result - R)
