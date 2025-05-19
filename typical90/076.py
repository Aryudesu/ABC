def calc(N: int, A: list):
    all = sum(A)
    if all % 10 != 0:
        return False
    target = all // 10
    data = []
    for a in A:
        data.append(a)
    for a in A:
        data.append(a)
    s = 0
    sdata = set()
    for d in data:
        s += d
        sdata.add(s)

    if target in sdata:
        return True

    for d in sdata:
        if d - target in sdata:
            return True

    return False


N = int(input())
A = [int(l) for l in input().split()]
print("Yes" if calc(N, A) else "No")
