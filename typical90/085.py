K = int(input())
result = 0
for a in range(1, K + 1):
    if a * a * a > K:
        break
    for b in range(a, K + 1):
        if a * b * b > K:
            break
        if K % (a * b) == 0:
            result += 1
print(result)
