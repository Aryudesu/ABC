S = []
for i in range(9):
    S.append(input())
count = 0
for w in range(81):
    a = w % 9
    b = w // 9
    if S[a][b] == "#":
        for x in range(w):
            c = x % 9
            d = x // 9
            if c >= a:
                if S[c][d] != "#":
                    continue
                if a + b - d >= 9 or a + b - d < 0:
                    continue
                if b + c - a >= 9 or b + c - a < 0:
                    continue
                if b + c - d >= 9 or b + c - d < 0:
                    continue
                if d + c - a >= 9 or d + c - a < 0:
                    continue
                if S[a + b - d][b + c - a] == "#" and S[b + c - d][d + c - a] == "#":
                    count += 1
            else:
                continue
print(count)
