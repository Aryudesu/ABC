def calc(N, A, data):
    result1 = 0
    result2 = 0
    for idx in range(N):
        if idx in data:
            result1 |= A[idx]
        else:
            result2 |= A[idx]
    return result1 ^ result2


def bit_all_search(A, M):
    """
    ビット全探索を行います
    A: 探索用配列
    M: 何個の要素で探索を行うか
    それ以降: 条件確認に用いるやつ
    """
    result = 10**100
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
        c = calc(M, A, data)
        if result > c:
            result = c
    return result


N = int(input())
A = [int(l) for l in input().split()]
print(bit_all_search(A, N))
