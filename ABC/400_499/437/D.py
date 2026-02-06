from bisect import bisect_left

def calc(N: int, M: int, A: list[int], B: list[int]):
    A.sort()
    s = 0
    S = [0]
    for a in A:
        s += a
        S.append(s)
    result = 0
    for b in B:
        idx = bisect_left(A, b)
        tmp1 = idx * b - S[idx]
        tmp2 = S[-1] - S[idx] - b * (N - idx)
        result = (result + tmp1 + tmp2) % 998244353
    return result


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(calc(N, M, A, B))
