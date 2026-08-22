N, R = map(int, input().split())
A = list(map(int, input().split()))
print(sum(A) - min(A) * N)
