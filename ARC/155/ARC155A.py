T = int(input())
result = []
for t in range(T):
    N, K = [int(l) for l in input().split()]
    S = input()
    # 少なくとも(N + K)が2Kの倍数であればK種類文字が入る余地がある
    # 0 3 4 7 8  ...
    # 1 2 5 6 9 ...
    # というようにギザギザに文字を検証していきたい
    if (N + K) % (2 * K) == 0:
        data = dict()
        # K文字分
        for idx in range(K):
            data[idx] = S[idx]
        for idx in range(1, N // K):
            # 上から下（forにイチイチifをかませるより良いかなと）
            if idx % 2 == 0:
                for idx2 in range(K):
                    s = S[idx * K + idx2]

            else:
                pass
    else:
        # NがK^2の倍数でなく文字が1種類以上あれば駄目
        prev = None
        for s in S:
            if prev is None:
                prev = s
            else:
                if s != prev:
                    result.append("No")
