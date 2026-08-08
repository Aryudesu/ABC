N = int(input())
V = list(map(int, input().split()))
V.sort()
result = 0
for n in range(N-1):
    result += V[n+1] - V[n]
print(result)
