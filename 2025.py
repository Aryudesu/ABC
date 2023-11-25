N = int(input())
result = set()
for x in range(N):
    if x**2 > N:
        break
    for y in range(N):
        if y**2 > N:
            break
        if x ** 2 + y ** 2 > N:
            break
        if x**2 + y**2 == N:
            result.add((x, y))
            result.add((-x, y))
            result.add((x, -y))
            result.add((-x, -y))
print(len(result))
print(result)
