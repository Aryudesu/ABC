N, M, K = map(int, input().split())
data = [1] * K + [0] * (N-K)
for m in range(M):
    a, b = map(int, input().split())
    data[b-1] = min(1, data[b-1] + data[a-1])
    data[a-1] = min(1, data[b-1] + data[a-1])
print(sum(data[i]!=0 for i in range(N)))
