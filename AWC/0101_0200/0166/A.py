N = int(input())
A = list(map(int, input().split()))
M = min(A)
print(sum(max(0, a-M) for a in A))
