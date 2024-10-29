def is_satisfy(A, data, SK):
    """与えられた条件を満たすか"""
    result = 0
    for dat in data:
        result += A[dat]
    return max([result, SK - result])


def bit_all_search(N, K):
    SK = sum(K)
    result = SK
    for a in range(1 << N):
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
        result = min([is_satisfy(K, data, SK), result])
    return result

N = int(input())
K = [int(l) for l in input().split()]
print(bit_all_search(N, K))
