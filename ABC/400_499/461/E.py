from collections import defaultdict

N, Q = map(int, input().split())
colNum = set()
rowNum = set()
result = 0
# 塗り直した行
redrawRow = defaultdict(set)
redrawNum = 0
for _ in range(Q):
    n, q = map(int, input().split())
    match n:
        case 1:
            r = q
            if r not in rowNum:
                result += N - len(colNum)
            rowNum.add(r)
        case 2:
            c = q
            if c not in colNum:
                result += N - len(rowNum)
            colNum.add(c)
        case _:
            raise ValueError()
    print(result)
print(result)
