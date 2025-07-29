from sortedcontainers import SortedList


def calc(N, M, A: SortedList, B: SortedList):
    result = 0
    memo = []
    for a in A:
        idx = B.bisect_left(M - a)
        if len(B) > idx and B[idx] == M - a:
            B.discard(M - a)
            memo.append(a)
    for m in memo:
        A.discard(m)
    idx = 0
    bidx = len(A) - 1
    while idx < len(A):
        if A[idx] + B[bidx] >= M:
            result += (A[idx] + B[bidx]) % M
            A.pop(idx)
            B.pop(bidx)
            bidx -= 1
        else:
            idx += 1
    for idx in range(len(A)):
        result += (A[idx] + B[idx]) % M
    return result

T = int(input())
result = []
for t in range(T):
    N, M = [int(l) for l in input().split()]
    A = SortedList([int(l) for l in input().split()])
    B = SortedList([int(l) for l in input().split()])
    result.append(calc(N, M, A, B))
for r in result:
    print(r)
