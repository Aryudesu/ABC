N, K = map(int, input().split())
A = list(map(int, input().split()))
data = [1] * N
# 反転範囲内か
f = 1
result = 0
for idx in range(N-K+1):
    if f == 1 and A[idx] == 1:
        result += 1
        # ON-OFF反転開始
        data[idx] *= -1
        # ON-OFF反転終了
        if idx + K - 1 < N:
            data[idx + K - 1] *= -1
    elif f == -1 and A[idx] == 0:
        result += 1
        # ON-OFF反転開始
        data[idx] *= -1
        # ON-OFF反転終了
        if idx + K - 1 < N:
            data[idx + K - 1] *= -1
    f *= data[idx]
isOk = True
for idx in range(N-K+1, N):
    if f == 1 and A[idx] == 1:
        isOk = False
    elif f == -1 and A[idx] == 0:
        isOk = False
    f *= data[idx]
if isOk:
    print(result)
else:
    print(-1)
