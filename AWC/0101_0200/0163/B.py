L, W = map(int, input().split())
result = 0
while L > W:
    L = (L+1)>>1
    result += 1
print(result)
