H, W = map(int, input().split())
data = [input().count(".") for _ in range(H)]
print(data.index(max(data)) + 1)
