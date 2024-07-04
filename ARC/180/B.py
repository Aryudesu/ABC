Memo = dict()
Memo2 = set()
def calc(data, N, K, depth):
    tmp = tuple(data)
    if tmp in Memo:
        return Memo.get(tmp, 0)
    swF = False
    result = 0
    mi, mj = None, None
    for i in range(N - K + 1):
        for j in range(i + 1, N):
            if data[i] > data[j]:
                if not (i, j) in Memo2:
                    data[i], data[j] = data[j], data[i]
                    Memo2.add((i, j))
                    tmp = calc(data, N, K, depth + 1)
                    Memo2.remove((i, j))
                    data[i], data[j] = data[j], data[i]
                    if result < tmp:
                        result = tmp
                swF = True
    if not swF:
        Memo[tuple(data)] = 0
        return depth
    # そこまでにいくら溜まっているか
    if not (mi is None) and not (mj is None):
        tmp1 = tuple(data)
        tmp2 = Memo.get(tmp1, 0)
        if tmp2 < result - depth:
            Memo[tuple(data)] = result - depth
    return result

N, K = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
print(calc(P, N, K, 0))
