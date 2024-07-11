def calc_cost(N, i, S):
    # N: 文字数
    # i: インデックス
    # S: 文字列
    K = N // 2
    res = 0
    for k in range(K):
        a = (i+k) % N
        b = (i-k-1) % N
        # print(a, b)
        if S[a] != S[b]:
            res += 1
    return res


N, A, B = [int(l) for l in input().split()]
S = input()
cost = (A + B) * N
for n in range(N):
    c = calc_cost(N, n, S) * B + n * A
    if cost > c:
        cost = c
print(cost)
