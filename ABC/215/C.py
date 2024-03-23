from itertools import permutations

S, K = [l for l in input().split()]
K = int(K)
S = list(S)
data = set()
for dat in permutations(S):
    data.add("".join(dat))
data_list = list(data)
data_list.sort()
# print(data_list)
print(data_list[K-1])
