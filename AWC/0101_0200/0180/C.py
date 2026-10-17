N = int(input())
A = list(map(int, input().split()))
data = [(A[idx], idx + 1) for idx in range(N)]
data.sort()
result = [dat[1] for dat in data]
print(*result)
