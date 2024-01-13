N, K = [int(l) for l in input().split()]
if (K - (N-1) * 2) % 2 == 0:
    print("Yes")
else:
    print("No")
