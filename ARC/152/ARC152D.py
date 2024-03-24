def calc():
    N, K = [int(l) for l in input().split()]
    Nums = [(i + K) % N for i in range(N)]
    res = []
    # 偶数のときは絶対無理
    if N % 2 == 0:
        res.append([-1])
        return res
    yet = set()
    res.append([(N-1)//2])
    count = 0
    for k in range(N):
        for l in range(k):
            if (k, l) not in yet and ((k + K) % N, (l + K) % N) not in yet and (l, k) not in yet and ((l + K) % N, (k + K) % N) not in yet:
                res.append([k, l])
                yet.add((k, l))
                yet.add((l, k))
                yet.add(((k + K) % N, (l + K) % N))
                yet.add(((l + K) % N, (k + K) % N))
                count += 1
                if count >= (N - 1) // 2:
                    break
    if count != (N - 1) // 2:
        return [[-1]]
    return res


res = calc()
for r in res:
    print(*r)
