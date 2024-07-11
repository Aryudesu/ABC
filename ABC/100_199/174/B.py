N, D = [int(l) for l in input().split()]
D2 = D ** 2
result = 0
for n in range(N):
    x, y = [int(l) for l in input().split()]
    if x ** 2 + y ** 2 <= D2:
        result += 1
print(result)
