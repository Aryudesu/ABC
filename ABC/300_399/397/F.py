import sys
from collections import defaultdict


def max_unique_types(N, A):
    # 左側のユニーク数カウント
    left_unique = [0] * N
    seen = set()
    for i in range(N):
        seen.add(A[i])
        left_unique[i] = len(seen)

    # 右側のユニーク数カウント
    right_unique = [0] * N
    seen.clear()
    for j in range(N-1, -1, -1):
        seen.add(A[j])
        right_unique[j] = len(seen)

    # 最大値を探索
    max_types = 0
    seen_middle = set()
    j = 1  # 中央の開始位置（i < j の条件を満たす最小 j）

    for i in range(N-2):  # i の範囲は 0 から N-3 まで
        seen_middle.add(A[i])
        while j < N-1 and A[j] not in seen_middle:
            seen_middle.add(A[j])
            j += 1

        # (i, j) の時点での最大種類数を計算
        if j < N-1:
            middle_count = len(seen_middle)
            max_types = max(max_types, left_unique[i] + middle_count + right_unique[j])

        # i を進めるので中央から削除
        seen_middle.remove(A[i])

    return max_types

# 入力処理
N = int(input())
A = [int(l) for l in input().split()]
print(max_unique_types(N, A))
