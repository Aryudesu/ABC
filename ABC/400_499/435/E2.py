from sortedcontainers import SortedSet

class IntervalManager:
    """グリッドの区間をSortedSetで管理するやつ"""
    def __init__(self):
        self.intervals = SortedSet()
        self.total = 0

    def add(self, L, R) -> int:
        mergedL, mergedR = L, R
        idx = self.intervals.bisect_left((L, -10**18))

        if idx > 0 and self.intervals[idx - 1][1] + 1 >= L:
            idx -= 1

        removed = 0
        start_idx = idx

        while idx < len(self.intervals) and self.intervals[idx][0] <= R + 1:
            l0, r0 = self.intervals[idx]
            mergedL = min(mergedL, l0)
            mergedR = max(mergedR, r0)
            removed += r0 - l0 + 1
            idx += 1

        for _ in range(idx - start_idx):
            self.intervals.pop(start_idx)

        self.intervals.add((mergedL, mergedR))
        added = mergedR - mergedL + 1

        delta = added - removed
        self.total += delta
        return delta

im = IntervalManager()
N, Q = map(int, input().split())
for _ in range(Q):
    L, R = map(int, input().split())
    im.add(L, R)
    print(N - im.total)

