import heapq


class KLargestTriplet:
    def __init__(self, N:int, A:list, B:list, C:list):
        assert N == len(A)
        assert N == len(B)
        assert N == len(C)
        self.A = A
        self.B = B
        self.C = C
        self.A.sort(reverse=True)
        self.B.sort(reverse=True)
        self.C.sort(reverse=True)

    def calcNum(self, i:int, j:int, k:int) -> int:
        return self.A[i] * self.B[j] + self.B[j] * self.C[k] + self.C[k] * self.A[i]

    def calc(self, K:int) -> int:
        data = []
        memo = set()
        i, j, k = 0, 0, 0
        heapq.heapify(data)
        heapq.heappush(data, (-self.calcNum(i, j, k), i, j, k))
        memo.add((i, j, k))
        for _ in range(K-1):
            _, i, j, k = heapq.heappop(data)
            if i + 1 < N and not (i + 1, j, k) in memo:
                tmp = -self.calcNum(i + 1, j, k)
                heapq.heappush(data, (tmp, i + 1, j, k))
                memo.add((i + 1, j, k))
            if j + 1 < N and not (i, j + 1, k) in memo:
                tmp = -self.calcNum(i, j + 1, k)
                heapq.heappush(data, (tmp, i, j + 1, k))
                memo.add((i, j + 1, k))
            if k + 1 < N and not (i, j, k + 1) in memo:
                tmp = -self.calcNum(i, j, k + 1)
                heapq.heappush(data, (tmp, i, j, k + 1))
                memo.add((i, j, k + 1))
        return -heapq.heappop(data)[0]

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]
klt = KLargestTriplet(N, A, B, C)
print(klt.calc(K))
