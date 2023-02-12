def is_satisfy(A, data, N):
    """与えられた条件を満たすか"""
    result = 0
    for dat in data:
        result |= A[dat]
    return result == N


def bit_all_search(A, M, N):
    """
    ビット全探索を行います
    A: 探索用配列
    M: 何個の要素で探索を行うか
    それ以降: 条件確認に用いるやつ
    """
    result = 0
    for a in range(1 << M):
        data = []
        tmp = a
        count = 0
        # Bit全探索用に配列作成
        while tmp:
            if tmp & 1:
                data.append(count)
            count += 1
            tmp >>= 1
        # 条件を満たす場合の処理
        if is_satisfy(A, data, N):
            result += 1
    return result


# ABC289C
N, M = [int(l) for l in input().split()]
Ma = (1 << N) - 1
data = {0: 1}
A = []
for m in range(M):
    Q = int(input())
    num = [int(l) for l in input().split()]
    tmp = 0
    for n in num:
        tmp += 1 << (n-1)
    A.append(tmp)
print(bit_all_search(A, M, Ma))
