def calcAll(AB: list[list[int]]) -> float:
    result = 0
    for a, b in AB:
        result += a/b
    return result

def calcTime(AB: list[list[int]], time: float) -> float:
    result = 0
    t = 0
    for a, b in AB:
        if t + a/b < time:
            t += a/b
            result += a
        else:
            result += (time - t)*b
            break
    return result

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
allTime = calcAll(AB)
print(calcTime(AB, allTime/2))

