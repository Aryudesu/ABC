def subset_sum_bitset(A: list[int], target: int) -> bool:
    """
    正の整数列 A から部分和 target を作れるかどうかを判定する。
    各要素は1回までしか使えない（01ナップサックと同様）。
    """
    bits = 1  # bitsの i 桁目が1 <=> 部分和 i が作れる
    for a in A:
        bits |= bits << a
        if (bits >> target) & 1:
            return True  # targetが作れたら即終了
    return (bits >> target) & 1


N, S = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print("Yes" if subset_sum_bitset(A, S) else "No")
