def calc():
    A = []
    col = []
    row = []
    cell = []
    for i in range(9):
        tmp = set()
        col.append(tmp)
        tmp = set()
        row.append(tmp)
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp2 = set()
            tmp.append(tmp2)
        cell.append(tmp)
    for n in range(9):
        A.append([int(l) for l in input().split()])
    for i in range(9):
        for j in range(9):
            a = A[i][j]
            c = col[j]
            if a in c:
                return False
            c.add(a)
            col[j] = c
            r = row[i]
            if a in r:
                return False
            r.add(a)
            row[i] = r
            ce = cell[i//3][j//3]
            if a in ce:
                return False
            ce.add(a)
            cell[i//3][j//3] = ce
    return True


print("Yes" if calc() else "No")
