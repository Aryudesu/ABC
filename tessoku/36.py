N, K = [int(l) for l in input().split()]
print("Yes" if K >= 2 * (N-1) and (K - (N-1) * 2) % 2 == 0 else "No")
