S, T = map(int, input().split())
result = 0
for a in range(S + 1):
    for b in range(S + 1):
        if a + b > S:
            break
        for c in range(S + 1):
            if a + b + c > S:
                break
            if a * b * c > T:
                break
            result += 1
print(result)
