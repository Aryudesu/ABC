N = int(input())
result = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        result.append("H")
    elif a == b:
        result.append("E")
    else:
        result.append("L")
print("".join(result))
