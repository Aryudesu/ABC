def isOk(H: int, W: int, y1: int, x1: int, y2: int, x2: int, S: list[str])->bool:
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if S[y1 + y2 - y][x1 + x2 - x] != S[y][x]:
                return False
    return True

def calc(H:int, W: int, S: list[str])->int:
    result = 0
    for h1 in range(H):
        for w1 in range(W):
            for h2 in range(h1, H):
                for w2 in range(w1, W):
                    if isOk(H, W, h1, w1, h2, w2, S):
                        result += 1
    return result


H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(input())
print(calc(H, W, S))
