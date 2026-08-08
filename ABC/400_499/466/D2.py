N, M = map(int, input().split())
RC = []
row, col = set(), set()
for _ in range(M):
    RC.append(map(int, input().split()))
RC.reverse()
result = 0
for r, c in RC:
    if r not in row and c not in col:
        result += 1
    row.add(r)
    col.add(c)
print(result)
