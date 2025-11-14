N = list(map(int, input().split()))
N.sort()
print(N[2] if N[0] == N[1] else N[0])
