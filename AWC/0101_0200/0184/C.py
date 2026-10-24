N, M = map(int, input().split())
D = list(map(int, input().split())) + [-1]
S = list(map(int, input().split()))
D.sort()
# print(D)
result = []
for s in S:
    res = 0
    for idx in range(M.bit_length(), -1, -1):
        b = 1 << idx
        if (res | b) <= M and D[res | b] <= s:
            res |= b
    result.append(res)
print(*result, sep="\n")
