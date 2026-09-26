from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
result = 0
for data in permutations(A):
    tmp = 0
    for i in range(N-1):
        tmp += abs(data[i] - data[i+1])
    result = max(result, tmp)
print(result)
