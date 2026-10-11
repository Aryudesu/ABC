H, W = map(int, input().split())
print(max(input().count("x") for _ in range(H)))
