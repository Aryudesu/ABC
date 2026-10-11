H, W = map(int, input().split())
print("Yes" if sum("o" in input() for _ in range(H)) == H else "No")
