N = int(input())
A = [int(l) for l in input().split()]
data = [(A[i], i + 1) for i in range(N)]
data.sort(reverse=True)
print(data[1][1])
