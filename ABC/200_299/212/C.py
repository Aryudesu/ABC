from sortedcontainers import SortedList


def calc(A: SortedList, B: SortedList):
    result = 10 ** 11
    for a in A:
        tmp = B.bisect_left(a)
        for i in range(-1, 2):
            if tmp + i >= 0 and tmp + i < len(B):
                result = min([result, abs(a - B[tmp + i])])
    return result


N, M = [int(l) for l in input().split()]
A = SortedList(int(l) for l in input().split())
B = SortedList(int(l) for l in input().split())
print(calc(A, B))
