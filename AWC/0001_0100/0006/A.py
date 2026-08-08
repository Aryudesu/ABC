N, L, W = map(int, input().split())
D = list(map(int, input().split()))
result = 0
for d in D:
    result += 1 if L-W <= d <= L+W else 0
print(result)
