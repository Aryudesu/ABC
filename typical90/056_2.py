def existsSubset(arr: list[int], K: int) -> list[bool]|None:
    if K < 0:
        return None
    N = len(arr)
    result = [False] * N
    data = []
    dp = [False] * (K + 1)
    dp[0] = True
    for i in range(N):
        a = arr[i]
        newDP = dp.copy()
        for k in range(K+1):
            if not dp[k]:
                continue
            if a + k > K:
                continue
            newDP[a + k] = True
        dp = newDP
        data.append(dp.copy())
    if not data[-1][K]:
        return None
    data.reverse()
    arr.reverse()
    target = K
    for i in range(N - 1):
        if data[i+1][target]:
            target = target
        else:
            target = target - arr[i]
            result[i] = True
    if target != 0:
        result[-1] = True
    result.reverse()
    return result

N, S = map(int, input().split())
sm = 0
memo = []
nums = []
for n in range(N):
    a, b = map(int, input().split())
    if a < b:
        sm += a
        memo.append(0)
        nums.append(b - a)
    else:
        sm += b
        memo.append(1)
        nums.append(a - b)
res = existsSubset(nums, S - sm)
if res is None:
    print("Impossible")
else:
    result = ""
    T = "AB"
    for i in range(N):
        if res[i]:
            result += T[1 - memo[i]]
        else:
            result += T[memo[i]]
    print(result)

