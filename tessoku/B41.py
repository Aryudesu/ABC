def calc(X: int, Y: int) -> list[list[int]]:
    x, y = X, Y
    result = []
    while x > 1 or y > 1:
        result.append([x, y])
        if x > y:
            x, y = x - y, y
        else:
            x, y = x, y - x
    result.reverse()
    return result


X, Y = map(int, input().split())
res = calc(X, Y)
print(len(res))
for r in res:
    print(*r)
