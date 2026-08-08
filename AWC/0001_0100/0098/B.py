N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
sData = []
for n in range(N):
    sData.append((S[n], n))
T.sort(reverse=True)
sData.sort(reverse=True)
result = [None] * N
count = 0
while sData:
    s, idx = sData.pop()
    while T and T[-1] <= s:
        T.pop()
        count += 1
    result[idx] = count
for res in result:
    print(res)
