from typing import Tuple

def calc90(N: int, y: int, x: int)->list[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    result = [(y, x)]
    for _ in range(3):
        nowY, nowX = result[-1]
        nextY, nextX = nowX, N - 1 - nowY
        result.append((nextY, nextX))
    return result

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
field = [[False for _ in range(N)] for _ in range(N)]
data = []
center = None
for h in range(N):
    for w in range(N):
        if field[h][w]:
            continue
        if N & 1 and w == h == N // 2:
            center = A[h][w]
            continue
        tmp = []
        points = calc90(N, h, w)
        for py, px in points:
            field[py][px] = True
            tmp.append(A[py][px])
        data.append(sum(tmp))
data.sort()
kNum = K
result = 0
while kNum > 0 and data:
    num = data.pop()
    match num:
        case 4:
            result += 4
        case 3:
            kNum -= 1
            result += 4
        case 2:
            if kNum >= 2:
                result += 4
                kNum -= 2
            else:
                kNum -= 1
                result += 2
        case 1:
            if kNum >= 1 and center is not None:
                center = None
                result += 1
                kNum -= 1
            if kNum >= 3:
                result += 4
                kNum -= 3
            elif kNum >= 2:
                result += 2
                kNum -= 2
            elif kNum >= 1:
                result += 1
                kNum -= 1
        case 0:
            if kNum >= 1 and center is not None:
                center = None
                result += 1
                kNum -= 1
            if kNum >= 4:
                result += 4
                kNum -= 4
            elif kNum >= 3:
                result += 2
                kNum -= 3
            elif kNum >= 2:
                result += 2
                kNum -= 1
print(result)
