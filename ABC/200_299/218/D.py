def calc(N: int, XY:list[tuple[int]]) -> int:
    result = 0
    pointData = set(XY)
    memo = set()
    for i in range(N-1):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y1, x2, y2) in memo:
                continue
            if not (x1, y2) in pointData:
                continue
            if not (x2, y1) in pointData:
                continue
            memo.add((x1, y2, x2, y1))
            memo.add((x2, y1, x1, y2))
            result += 1
    return result


N = int(input())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
print(calc(N, XY))
