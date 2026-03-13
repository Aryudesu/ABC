N, X = map(int, input().split())
A = list(map(int, input().split()))
print(sum(a < X for a in A))
