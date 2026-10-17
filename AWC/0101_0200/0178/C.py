N, K, M = map(int, input().split())
D = []
for _ in range(K):
    b, d = map(int, input().split())
    D.append(d)
D.sort()
result = 0
c = 0
while D:
    result += D[-1] * 2
    for _ in range(M):
        if not D:
            break
        d = D.pop()
print(result)
