N = int(input())
result = set()
for n in range(N):
    a, b = [int(l) for l in input().split()]
    if a == 0 or b == 0:
        result.add(n + 1)
    else:
        if a in result:
            result.add(n + 1)
        if b in result:
            result.add(n + 1)
print(len(result))
