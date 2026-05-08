def calc(A1: list[int], A2: list[int], A3: list[int]):
    res = 0
    dat = (4, 5, 6)
    for a in A1:
        for b in A2:
            for c in A3:
                tmp = tuple(sorted([a, b, c]))
                if tmp == dat:
                    res += 1
    return res

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
print(calc(A1, A2, A3)/(6 ** 3))
