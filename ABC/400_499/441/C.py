def calc(N: int, K: int, X: int, A:list[int])->int:
    A.sort()
    # 多い方からN-Kは全部水であるとする
    result = N - K
    # 残ったK個のうち多い順に飲んでいく
    S = 0
    for i in range(K):
        a = A[K-i-1]
        S += a
        result += 1
        if S >= X:
            return result
    return -1


N, K, X = map(int, input().split())
A = list(map(int, input().split()))
print(calc(N, K, X, A))
