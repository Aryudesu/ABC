N = int(input())
T = list(map(int, input().split()))
m = 10000000
M = 0
for i in range(N-1):
    d = T[i+1]-T[i]
    m = min(m, d)
    M = max(M, d)
print(m, M)
