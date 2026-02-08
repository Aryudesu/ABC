def doubling(N: int, B: int, C: list[int], maxLen: int = 62):
    MOD = 10 ** 9 + 7
    resultData = [[0] * B]
    # 1桁目
    for c in C:
        resultData[0][c] += 1
    # 各桁計算
    pow10 = 10
    idx = 0
    for _ in range(maxLen):
        nextData = [0] * B
        for b in range(B):
            for c in C:
                i = (b * pow10 + c) % B
                nextData[i] = (nextData[i] + resultData[idx][b] * resultData[idx][c]) % MOD
        resultData.append(nextData)
        pow10 = (pow10 * pow10) % B
        idx += 1
    return resultData

def calc(N, B, C):
    data = doubling(N, B, C)
    return data[-1][0]

N, B, K = [int(l) for l in input().split()]
C = [int(l) % B for l in input().split()]
print(calc(N, B, C))
