N = int(input())
A = [int(l) for l in input().split()]
res = [None] * (2 * N + 2)
res[0], res[1] = 0, 0
for n in range(1, N + 1):
    # 分裂するアメーバ
    a = A[n - 1]
    # アメーバnが何代目か
    tmp = res[a]
    res[n * 2] = tmp + 1
    res[n * 2 + 1] = tmp + 1
for i in range(1, 2 * N + 2):
    print(res[i])
