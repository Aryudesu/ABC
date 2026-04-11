N = int(input())
H = list(map(int, input().split()))
result = [1]
for idx in range(1, N):
    h = H[idx]
    if H[result[-1]-1] < h:
        result.append(idx+1)
print(*result)
