N, M = map(int, input().split())
S, T = map(int, input().split())
PV = []
for m in range(M):
    p, v = map(int, input().split())
    PV.append((p, v))
PV.sort()
result = 0
for p, v in PV:
    if S <= p <= T:
        result += v
    elif T <= p <= S:
        result += v
print(result)
