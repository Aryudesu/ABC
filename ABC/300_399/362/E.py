N = int(input())
A = [int(l) for l in input().split()]
MOD = 998244353
result = [0] * N
# data[何個目] = {公差: [1個, 2個, 3個, ...]}
data = []
data.append(dict())
# 対象の項
for i in range(1, N):
    # その項についてのデータ
    new_data = dict()
    # それ以前の配列を全走査
    for j in range(i):
        # 公差
        data_j = data[j]
        kousa = A[i] - A[j]
        new_kousa = new_data.get(kousa, [0] * N)
        new_kousa[0] = 1
        j_kousa = data_j.get(kousa, [0] * N)
        if j_kousa[0] == 0:
            j_kousa[0] = 1
        for k in range(N - 1):
            new_kousa[k + 1] = (new_kousa[k + 1] + j_kousa[k]) % MOD
        new_data[kousa] = new_kousa
        # new_data[kousa] = new_data.get(kousa, 0) + data_j.get(kousa, 1)
    for k in new_data:
        v = new_data.get(k, [0] * N)
        for n in range(N):
            result[n] = (result[n] + v[n]) % MOD
    data.append(new_data)
result[0] = N
# print(data)
print(*result)
