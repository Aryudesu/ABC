def calc(N: int, K: int, A: list[int])->int:
    MOD = 10 ** 9 + 7
    s = A[0]
    k = K
    breakF = False
    for idx in range(1, N):
        a = A[idx]
        if a == s:
            continue
        # 差分全部埋めたい
        m = idx * (a - s)
        # print("debug", a, s, m, k)
        # 埋めることができる場合
        if m < k:
            s = a
            k -= m
        else:
            if idx == 0:
                breakF = True
                break
            # 埋められるだけ埋める
            s += k // idx
            k = k % idx
            for idx in range(k):
                A[idx] = s + 1
            for idx in range(k, N):
                A[idx] = max(A[idx], s)
            k = 0
            breakF = True
            break
    if not breakF:
        s += k // N
        k = k % N
    # print(k)
    for idx in range(k):
        A[idx] = s + 1
    for idx in range(k, N):
        A[idx] = max(A[idx], s)
    # print(A)
    result = 1
    for a in A:
        result = (result * a) % MOD
    return result

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = calc(N, K, A)
print(result)
