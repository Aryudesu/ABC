from sortedcontainers import SortedSet


class IntervalManager:
    def __init__(self):
        self.intervals = SortedSet()

    def add(self, L, R):
        """範囲を追加します"""
        merged = (L, R)

        idx = self.intervals.bisect_left(merged)
        if idx > 0 and self.intervals[idx - 1][1] + 1 >= L:
            idx -= 1
        to_remove = []
        while idx < len(self.intervals) and self.intervals[idx][0] <= R + 1:
            merged = (min(merged[0], self.intervals[idx][0]), max(merged[1], self.intervals[idx][1]))
            to_remove.append(self.intervals[idx])
            idx += 1
        for interval in to_remove:
            self.intervals.discard(interval)
        self.intervals.add(merged)

    def contains(self, num):
        """設定した範囲のいずれかに含まれるか"""
        idx = self.intervals.bisect_left((num, num))
        if idx < len(self.intervals) and self.intervals[idx][0] <= num <= self.intervals[idx][1]:
            return True
        if idx > 0 and self.intervals[idx - 1][0] <= num <= self.intervals[idx - 1][1]:
            return True
        return False

    def overlaps(self, L, R):
        """設定した範囲が重複している箇所があるか"""
        idx = self.intervals.bisect_left((L, L))
        if idx < len(self.intervals) and self.intervals[idx][0] <= R:
            return True
        if idx > 0 and self.intervals[idx - 1][1] >= L:
            return True
        return False

    def __repr__(self):
        return str(list(self.intervals))

# 使用例
manager = IntervalManager()
for i in range(50000):
    manager.add(3 * i, 3 * i + 1)
for i in range(50000 - 1, -1, -1):
    manager.add(0, 6000000)
print(manager)
