N, W = map(int, input().split())
L = list(map(int, input().split()))
L.reverse()
result = 0
S = 0
while L:
    if S + 1 + L[-1] > W:
        S = 0
    if S == 0:
        result += 1
    if S > 0:
        S += 1
    S += L.pop()
print(result)
