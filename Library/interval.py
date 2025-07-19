from sortedcontainers import SortedList


class AdvancedIntervalManager:
    def __init__(self):
        self.intervals = SortedList()
        self.total_length = 0

    def add(self, l, r):
        """区間 [l, r) を追加し、マージ＋区間長更新"""
        idx = self.intervals.bisect_left((l, r))
        if idx != 0 and self.intervals[idx - 1][1] >= l:
            idx -= 1

        merged_l, merged_r = l, r
        to_remove = []
        length_removed = 0

        while idx < len(self.intervals) and self.intervals[idx][0] <= r:
            merged_l = min(merged_l, self.intervals[idx][0])
            merged_r = max(merged_r, self.intervals[idx][1])
            length_removed += self.intervals[idx][1] - self.intervals[idx][0]
            to_remove.append(self.intervals[idx])
            idx += 1

        for interval in to_remove:
            self.intervals.remove(interval)

        self.intervals.add((merged_l, merged_r))
        self.total_length += (merged_r - merged_l) - length_removed

    def remove(self, l, r):
        """区間 [l, r) を削除し、区間長更新"""
        idx = self.intervals.bisect_left((l, r))
        if idx != 0 and self.intervals[idx - 1][1] > l:
            idx -= 1

        to_add = []
        to_remove = []
        length_removed = 0

        while idx < len(self.intervals) and self.intervals[idx][0] < r:
            a, b = self.intervals[idx]
            length_removed += min(b, r) - max(a, l)

            if a < l:
                to_add.append((a, min(b, l)))
            if r < b:
                to_add.append((max(a, r), b))
            to_remove.append(self.intervals[idx])
            idx += 1

        for interval in to_remove:
            self.intervals.remove(interval)
        for interval in to_add:
            self.intervals.add(interval)

        self.total_length -= length_removed

    def contains(self, x):
        """点 x が現在の区間集合に含まれるか"""
        idx = self.intervals.bisect_right((x, float('inf')))
        if idx == 0:
            return False
        return self.intervals[idx - 1][0] <= x < self.intervals[idx - 1][1]

    def covered(self, l, r):
        """区間 [l, r) が完全に被覆されているか"""
        idx = self.intervals.bisect_right((l, float('inf')))
        if idx == 0:
            return False
        a, b = self.intervals[idx - 1]
        return a <= l and r <= b

    def get_intervals(self):
        """現在の区間一覧を返す"""
        return list(self.intervals)

    def get_total_length(self):
        """現在の区間の合計長を返す"""
        return self.total_length

    def get_holes(self, L, R):
        """指定区間 [L, R) に存在する未被覆区間（穴）を返す"""
        holes = []
        current = L
        for a, b in self.intervals.irange((L, -float('inf')), (R, float('inf'))):
            if current < a:
                holes.append((current, min(a, R)))
            current = max(current, b)
            if current >= R:
                break
        if current < R:
            holes.append((current, R))
        return holes

    def get_intersections(self, l, r):
        """区間 [l, r) と被る区間のリストを返す"""
        intersections = []
        idx = self.intervals.bisect_left((l, r))
        if idx != 0 and self.intervals[idx - 1][1] > l:
            idx -= 1

        while idx < len(self.intervals) and self.intervals[idx][0] < r:
            a, b = self.intervals[idx]
            intersections.append((max(a, l), min(b, r)))
            idx += 1

        return intersections
