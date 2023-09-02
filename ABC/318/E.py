N = int(input())
A = [int(l) for l in input().split()]
data = dict()
dsum = dict()
dcount = dict()
result = 0
for n in range(N):
    a = A[n]
    tmp = data.get(a)
    tmp2 = dsum.get(a, 0)
    tmp3 = dcount.get(a, 0)
    # 直近の間に挟まっているやつ
    count = 0
    if not tmp is None:
        count = n - tmp - 1
        result += count * tmp3
    result += tmp2
    # 累計で挟まってるやつ
    dsum[a] = tmp2 + count * tmp3
    data[a] = n
    dcount[a] = tmp3 + 1
    # print(data)
print(result)
