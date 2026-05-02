N, X = map(int, input().split())
A = list(map(int, input().split()))
print(sum(max(0, a - X) for a in A))
