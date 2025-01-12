from sortedcontainers import SortedSet


class IntervalManager:
    def __init__(self):
        self.left_sorted = SortedSet()
        self.right_sorted = SortedSet()

    def add_interval(self, L, R):
        """新しい区間を追加し、必要なら統合"""
        if L > R:
            L, R = R, L
        left_idx = self.right_sorted.bisect_left((L, float('-inf')))
        right_idx = self.left_sorted.bisect_left((R + 1, float('-inf')))
        to_merge = []
        for i in range(left_idx, right_idx):
            l, r = self.left_sorted[i]
            to_merge.append((l, r))
        for l, r in to_merge:
            self.left_sorted.discard((l, r))
            self.right_sorted.discard((r, l))
            L = min(L, l)
            R = max(R, r)
        self.left_sorted.add((L, R))
        self.right_sorted.add((R, L))

    def get_intervals(self):
        """現在の区間リストを取得"""
        return list(self.left_sorted)

    def find_interval(self, point):
        """指定した点がどの区間に含まれているかを探す"""
        idx = self.right_sorted.bisect_left((point, float('-inf')))
        if idx < len(self.right_sorted):
            R, L = self.right_sorted[idx]
            if L <= point <= R:
                return (L, R)
        return None

    def check_overlap(self, L, R):
        """指定した区間が既存の区間と重複するかを判定"""
        if L > R:
            L, R = R, L

        idx = self.right_sorted.bisect_left((L, float('-inf')))
        if idx > 0:
            prev_R, prev_L = self.right_sorted[idx - 1]
            if prev_R >= L:
                return True
        idx = self.left_sorted.bisect_left((R + 1, float('-inf')))
        if idx < len(self.left_sorted):
            next_L, next_R = self.left_sorted[idx]
            if next_L <= R:
                return True

        return False
