N, K = [int(l) for l in input().split()]
S = input()
MOD = 998244353
data = dict()
sgdata = dict()

for s in S:
    data[s] = data.get(s, 0) + 1

sgdata['AB'] = data.get('A', 0) * data.get('B', 0)
sgdata['AC'] = data.get('A', 0) * data.get('C', 0)
sgdata['BC'] = data.get('B', 0) * data.get('C', 0)

# K = 0 のとき result = 1
result = 1
for k in range(1, K + 1):
    if k % 2:
        result = (result + sgdata['AB'] + sgdata['AC'] + sgdata['BC']) % MOD
    else:
        sgdata['AB'] = sgdata['AB'] - 1 if sgdata['AB'] > 0 else 0
        sgdata['AC'] = sgdata['AB'] - 1 if sgdata['AB'] > 0 else 0
        sgdata['BC'] = sgdata['AB'] - 1 if sgdata['AB'] > 0 else 0
print(result)
