N, D = map(int, input().split())
X = list(map(int, input().split()))
result = []
for i in range(N):
    isOk = True
    for j in range(N):
        if i == j:
            continue
        if abs(X[i] - X[j]) < D:
            isOk = False
            break
    if isOk:
        result.append(i+1)
print(len(result))
if result:
    print(*result)
