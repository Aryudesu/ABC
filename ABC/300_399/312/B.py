N, M = [int(l) for l in input().split()]
S = []
for n in range(N):
    S.append(input())

result = []
for y in range(N - 9 + 1):
    for x in range(M - 9 + 1):
        for dy in range(3):
            f = True
            if S[y + 3][x+3] != ".":
                f = False
                break
            if S[y + 5][x + 5] != ".":
                f = False
                break
            for dx in range(3):
                if S[y+dy][x+dx] != "#":
                    f = False
                    break
                if S[y+8-dy][x+8-dx] != "#":
                    f = False
                    break
            if not f:
                break
            if S[y + 3][x+dy] != ".":
                f = False
                break
            if S[y + dy][x+3] != ".":
                f = False
                break
            if S[y + 5][x + 6 + dy] != ".":
                f = False
                break
            if S[y + 6 + dy][x + 5] != ".":
                f = False
                break
        if f:
            result.append((y, x))
result.sort()
for r in result:
    y, x = r
    print(y+1, x+1)
