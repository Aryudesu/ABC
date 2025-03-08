from sortedcontainers import SortedSet


class IntervalManager:
    def __init__(self):
        self.intervals = SortedSet()

    def add(self, L, R):
        """ 区間 [L, R] を追加し、必要に応じて統合 """
        new_intervals = []
        merged = (L, R)
        
        # 既存の区間と統合できる最初の位置を取得
        idx = self.intervals.bisect_left(merged)
        if idx > 0 and self.intervals[idx - 1][1] + 1 >= L:
            idx -= 1

        # 統合可能な範囲を決定
        start_idx = idx
        while idx < len(self.intervals) and self.intervals[idx][0] <= R + 1:
            merged = (min(merged[0], self.intervals[idx][0]), max(merged[1], self.intervals[idx][1]))
            idx += 1
        
        # 統合される区間数
        merge_count = idx - start_idx

        if merge_count > len(self.intervals) * 0.3:
            # 大量の削除が発生するなら、新しい SortedSet に移行
            new_intervals = SortedSet(self.intervals[:start_idx] + self.intervals[idx:])
            new_intervals.add(merged)
            self.intervals = new_intervals
        else:
            # それ以外は通常の削除
            for _ in range(merge_count):
                self.intervals.pop(start_idx)
            self.intervals.add(merged)

    def contains(self, num):
        """ num がどこかの区間に含まれているかを判定 """
        idx = self.intervals.bisect_left((num, num))
        if idx < len(self.intervals) and self.intervals[idx][0] <= num <= self.intervals[idx][1]:
            return True
        if idx > 0 and self.intervals[idx - 1][0] <= num <= self.intervals[idx - 1][1]:
            return True
        return False

    def overlaps(self, L, R):
        """ 区間 [L, R] が既存の区間と重なっているかを判定 """
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
print(manager)
