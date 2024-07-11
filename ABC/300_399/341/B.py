N = int(input())
A = [int(l) for l in input().split()]
data = []
for i in range(N):
    data.append([A[i], i])
data.sort(reverse=True)
ST = []
for _ in range(N-1):
    ST.append([int(l) for l in input().split()])
print(data)
