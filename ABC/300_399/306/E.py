from sortedcontainers import SortedList


N, K, Q = map(int, input().split())
sortedData = SortedList([0] * N)
data = [0] * N
# 最初は全部0なのでk番目の値ももちろん0
kth = 0
sumdata = 0
result = []
for q in range(Q):
    X, Y = map(int, input().split())
    X -= 1
    # 書き換え前のk番目の値
    kth = -sortedData[K-1]
    # 書き換え前
    prev = data[X]
    now = Y
    data[X] = now
    # 書き換え前は外す
    sortedData.discard(-prev)
    sortedData.add(-now)
    next_kth = -sortedData[K - 1]
    # 入れる値が挿入後のk番目以下ならk番目の値を足す
    if now <= next_kth:
        sumdata += next_kth
    else:
        # 入れる値が挿入後のk番目より大きいなら挿入した値を足す
        sumdata += now
    # 外れる値が挿入後の大きいのであれば
    # 総和から削除
    if prev > next_kth:
        sumdata -= prev
    else:
        sumdata -= kth
    result.append(sumdata)
    # print(sortedData, data, sumdata, kth, prev, next_kth)
for r in result:
    print(r)
    
