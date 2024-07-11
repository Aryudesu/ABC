N, T = [int(l) for l in input().split()]
S = input()
X = [int(l) for l in input().split()]
Data = [(X[i], 1 if S[i] == "1" else -1) for i in range(N)]
Data.sort()
prevData = [(Data[i][0], Data[i][1], i) for i in range(N)]
prevData.sort()
# print(prevData)
aftData = [(x + (T+0.5) * s, i) for x, s, i in prevData]
aftData.sort()
result = 0
for n in range(N):
    x, i = aftData[n]
    result += abs(n - i)
print(result//2)
