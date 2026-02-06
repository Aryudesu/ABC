D, F = map(int, input().split())
result = 0
for i in range(F, D + 1, 7):
    result = i
print(i + 7 - D)
