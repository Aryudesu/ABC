N, P = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
result = 0
for s in S:
    P -= s
    if P < 0:
        break
    result += 1
print(result)
