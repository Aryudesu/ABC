N, T, A = [int(l) for l in input().split()]
m = min([T, A])
M = max([T, A])
m2 = m + (N - T - A)
print("Yes" if m2 < M else "No")
