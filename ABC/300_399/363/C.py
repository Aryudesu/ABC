from itertools import permutations


def prod(n):
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result


N, K = [int(l) for l in input().split()]
S = list(input())
# 各文字の個数数える
data = dict()
for s in S:
    data[s] = data.get(s, 0) + 1
d = 1
# 回文存在判定
two_num = 0
for k in data:
    d *= prod(data.get(k, 1))
    if data.get(k, 1) >= 2:
        two_num += (data.get(k, 1)//2) * 2
# 長さKの回文が存在しなければN!出力して終わり
if two_num + 1 < K:
    print(prod(N))
    exit()
# 存在する場合は総当たり
result = 0
memo = set()
for dat in permutations(S):
    if dat in memo:
        continue
    memo.add(dat)
    # idxから回文判定を開始
    for idx in range(N - K + 1):
        # 回文判定
        tmp = True
        for idx2 in range(K//2):
            if dat[idx + idx2] != dat[idx + K - 1 - idx2]:
                tmp = False
                break
        if tmp:
            result += 1
            break
print((prod(N) // d) - result)
