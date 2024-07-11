import itertools


C = [[int(l) for l in input().split()] for _ in range(3)]
field = [[False, False, False], [False, False, False], [False, False, False]]


# がっかりする場合
def check(h, w):
    if (C[h][(w + 1) % 3] == C[h][(w + 2) % 3]) and field[h][(w + 1) % 3] and field[h][(w + 2) % 3]:
        return True
    if (C[(h + 1) % 3][w] == C[(h + 2) % 3][w]) and field[(h + 1) % 3][w] and field[(h + 2) % 3][w]:
        return True
    if h == w:
        if (C[(h + 1) % 3][(w + 1) % 3] == C[(h + 2) % 3][(w + 2) % 3]) and field[(h + 1) % 3][(w + 1) % 3] and field[(h + 2) % 3][(w + 2) % 3]:
            return True
    if h == 2 - w:
        if (C[(h - 1) % 3][(w + 1) % 3] == C[(h - 2) % 3][(w + 2) % 3]) and field[(h - 1) % 3][(w + 1) % 3] and field[(h - 2) % 3][(w + 2) % 3]:
            return True
    field[h][w] = True
    return False


memo = set()
count = 0
bunbo = 0
for nums in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8]):
    tmp = []
    flag = False
    for i in nums:
        # がっかりしたらそこで打ち切り
        if check(i % 3, i // 3):
            tmp.append(i)
            flag = True
            break
    bunbo += 1
    if not flag:
        count += 1
    field = [[False, False, False], [
        False, False, False], [False, False, False]]
print(count/bunbo)
