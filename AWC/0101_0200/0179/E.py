from bisect import bisect_right

def lisLength(A: list[int]) -> int:
    """LISの長さのみを計算するO(N log N)"""
    dp = []
    for a in A:
        i = bisect_right(dp, a)
        if i == len(dp):
            dp.append(a)
        else:
            dp[i] = a
    return len(dp)

N = int(input())
A = list(map(int, input().split()))
length = lisLength(A)
print(N-length)
