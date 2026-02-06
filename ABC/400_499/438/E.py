N, Q = map(int, input().split())
A = list(map(int, input().split()))
data = [[A[i] for i in range(N)]]
for _ in range(1, 30):
    data.append([data[-1][data[-1][i]] for i in range(N)])
for _ in range(Q):
    input()
print(data)
