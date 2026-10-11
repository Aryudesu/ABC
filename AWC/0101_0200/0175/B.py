H, W, K = map(int, input().split())
print("".join(input()[K-1] for _ in range(H)))
