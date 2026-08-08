N, S, T = map(int, input().split())
A = list(map(int, input().split()))
print(sum(abs(a - S) <= T for a in A))
