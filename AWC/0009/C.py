N, T, K = map(int, input().split())
TK = T + K
H = list(map(int, input().split()))
H.sort()
minH = H[0]
result = 0
for h in H:
    if h - minH + 1 <= TK:
        result += 1
print(result)
