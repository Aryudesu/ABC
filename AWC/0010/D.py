def calc(N: int, K: int, H: list[int])->int:
    if N <= K:
        return N
    H.sort(reverse=True)
    result = K
    H = H[K:]
    result += sum(H)
    return result


N, K = map(int, input().split())
H = list(map(int, input().split()))
print(calc(N, K, H))
