N = int(input())
A = list(map(int, input().split()))
A.sort()
sa = sum(A)
d = sa % N
target = sa // N
result = 0
for a in A[:N-d]:
    result += abs(target - a)
for a in A[N-d:]:
    result += abs(target + 1 - a)
result //= 2
print(result)
