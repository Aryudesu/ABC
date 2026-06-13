from typing import Sequence, TypeVar

T = TypeVar("T")


def myers_distance(a: Sequence[T], b: Sequence[T]) -> int:
    """
    Myers の O(ND) アルゴリズムで、挿入＋削除のみの編集距離を求める。

    Parameters
    ----------
    a, b : 任意のシーケンス（str, list, tuple など）

    Returns
    -------
    d : int
        a を b に変換するのに必要な insert + delete の最小回数。
        （置換は insert+delete 2回としてカウントされる）
    """
    n, m = len(a), len(b)
    max_d = n + m

    # v[k] = 対角線 k 上で到達できる最大の x
    # 論文では配列 V[-MAX..MAX] だが、Python では dict でやる
    v = {1: 0}

    for d in range(max_d + 1):
        # d 回の編集（非対角辺）を使うパスを全部試す
        for k in range(-d, d + 1, 2):
            # どっちから来たか？
            #   k-1 → 右（delete）
            #   k+1 → 下（insert）
            if k == -d or (k != d and v.get(k - 1, 0) < v.get(k + 1, 0)):
                # 下から来る（insert）
                x = v.get(k + 1, 0)
            else:
                # 右から来る（delete）
                x = v.get(k - 1, 0) + 1

            y = x - k

            # snake：一致する限り対角線を貪欲に伸ばす
            while x < n and y < m and a[x] == b[y]:
                x += 1
                y += 1

            v[k] = x

            # 終点 (n, m) に到達したらそれが最小 d
            if x >= n and y >= m:
                return d

    # ここまで行くことは理論上ないが、お守りで
    return max_d


def lcs_length(a: Sequence[T], b: Sequence[T]) -> int:
    """
    Myers の距離から LCS の長さを求めるユーティリティ関数。
    """
    d = myers_distance(a, b)
    return (len(a) + len(b) - d) // 2

S = [int(l) for l in input()]
T = [int(l) for l in input()]
K = int(input())
Smemo = [S[0], S[-1]]
Tmemo = [T[0], T[-1]]
result = 0
for b in range(1 << 4):
    if b.bit_count() > K:
        continue
    if b & 1:
        S[0] = 1 - Smemo[0]
    else:
        S[0] = Smemo[0]
    if b & 2:
        S[-1] = 1 - Smemo[-1]
    else:
        S[-1] = Smemo[-1]
    if b & 4:
        T[0] = 1 - Tmemo[0]
    else:
        T[0] = Tmemo[0]
    if b & 8:
        T[-1] = 1 - Tmemo[-1]
    else:
        T[-1] = Tmemo[-1]
    L = lcs_length(S, T)
    result = max(result, L)
print(result)
