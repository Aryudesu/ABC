N = int(input())
A = list(map(int, input().split()))
M = max(A)
print(sum(M - a for a in A))
