H, W, Y, X = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())
T = input()
result = 0
memo = set()
x, y = X - 1, Y - 1
for t in T:
    if t == "L":
        dy = 0
        dx = -1
    elif t == "R":
        dy = 0
        dx = 1
    elif t == "U":
        dy = -1
        dx = 0
    elif t == "D":
        dy = 1
        dx = 0
    if x + dx < 0 or x + dx >= W:
        continue
    if y + dy < 0 or y + dy >= H:
        continue
    if S[y + dy][x + dx] == "#":
        continue
    y = y + dy
    x = x + dx
    # print(y, x, result)
    tmp = tuple([y, x])
    if S[y][x] == "@" and not tmp in memo:
        result += 1
        memo.add(tmp)
print(y + 1, x + 1, result)
