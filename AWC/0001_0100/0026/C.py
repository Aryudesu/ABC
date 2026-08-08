N, T, E = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
result = 0
s = 0
for p in P:
    tmp = p * T
    if s + tmp > E:
        break
    s += tmp
    result += 1
print(result)
