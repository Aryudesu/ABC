from sortedcontainers import SortedList

class BestKthSum:
    """
    上位K番目の値の総和を計算します．
    値の更新がされることを考慮．
    """

    def __init__(self, K: int, values: list[int]):
        assert 0 <= K <= len(values)
        self.k = K
        self.data = values[:]
        self.n = len(values)

        self.large = SortedList()
        self.small = SortedList()
        self.sum = 0

        for i, v in enumerate(self.data):
            self.small.add((v, i))

        for _ in range(self.k):
            if not self.small:
                break
            v, i = self.small.pop()
            self.large.add((v, i))
            self.sum += v

    def _rebalance(self):
        K = self.k

        while len(self.large) > K:
            v, i = self.large.pop(0)
            self.small.add((v, i))
            self.sum -= v

        while len(self.large) < K and self.small:
            v, i = self.small.pop()
            self.large.add((v, i))
            self.sum += v

        while self.large and self.small and self.large[0][0] < self.small[-1][0]:
            v_small, i_small = self.large.pop(0)
            v_big,   i_big   = self.small.pop()

            self.large.add((v_big, i_big))
            self.small.add((v_small, i_small))

            self.sum += v_big - v_small

    def update(self, idx: int, new_val: int) -> int:
        old_val = self.data[idx]
        if old_val == new_val:
            return self.sum

        self.data[idx] = new_val
        old_pair = (old_val, idx)

        if old_pair in self.large:
            self.large.remove(old_pair)
            self.sum -= old_val
        else:
            self.small.remove(old_pair)

        new_pair = (new_val, idx)
        self.large.add(new_pair)
        self.sum += new_val

        self._rebalance()
        return self.sum

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
data = [-A[m] for m in range(M)]
bks = BestKthSum(K, data)
result = []
for i in range(N-M+1):
    result.append(-bks.update((i+M-1)%M, -A[i+M-1]))
print(*result)
