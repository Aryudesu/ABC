N, M, K = map(int, input().split())
T = input()
S = []
tNums = [0] * K
for n in range(N):
    s = input()
    tmp = []
    for k in range(K):
        tmp.append(T[k] == s[k])
        tNums[k] += tmp[-1]
    S.append(tmp)
for s in S:
    print(s)
print(tNums)
Q = int(input())

for _ in range(Q):
    i, j = map(int, input().split())
