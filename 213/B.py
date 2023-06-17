N = int(input())
A = [int(l) for l in input().split()]
data = [(A[i], i + 1) for i in range(N)]
data.sort()
print(data[-2][1])
