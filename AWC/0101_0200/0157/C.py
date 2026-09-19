N, M, S = map(int, input().split())
pos = S
bound = 0
for n in range(N):
    c, a = input().split()
    a = int(a)
    dir = None
    match c:
        case "L":
            dir = -1
        case "R":
            dir = 1
        case _:
            raise ValueError()
    if a == 0:
        continue
    boundNum = (a // (2 * M)) * 2
    if a % (2 * M) == 0 and (pos == 0 or pos == M):
        boundNum = max(0, boundNum -1)
    if (pos == 0 and dir < 0 and a > 0) or (pos == M and dir > 0 and a > 0):
        boundNum += 1
    bound += boundNum
    a = a % (2 * M)
    if dir > 0:
        nextPos = pos + a
        if nextPos > M:
            bound += 1
            nextPos = M - (nextPos - M)
        if nextPos < 0:
            bound += 1
            nextPos = -nextPos
    else:
        nextPos = pos - a
        if nextPos < 0:
            bound += 1
            nextPos = -nextPos
        if nextPos > M:
            bound += 1
            nextPos = M - (nextPos - M)
    pos = nextPos
print(pos, bound)
