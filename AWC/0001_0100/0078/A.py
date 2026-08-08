N, M = map(int, input().split())
R = list(map(int, input().split()))
result = 0
for m in range(M):
    f, s = map(int, input().split())
    if R[f-1] < s:
        continue
    R[f-1] -= s
    result += 1
print(result)
