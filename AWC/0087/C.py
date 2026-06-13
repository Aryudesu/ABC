from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
data = [0]
for i in range(N-1):
    data.append(data[-1] + abs(A[i] - A[i+1]))
if data[-1] < K:
    print(-1)
    exit()
result = N * 2
for r in range(len(data)):
    d = data[r]
    lh = d - K
    if lh < 0:
        continue
    l = bisect_right(data, lh)
    if d - data[l] < K:
        l -= 1
    result = min(result, r - l + 1)
print(result)
