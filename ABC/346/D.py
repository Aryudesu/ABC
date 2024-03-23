# なんで通らないのおおおおおおおおおおおおおおおおおおおおお
N = int(input())
S = input()
C = [int(l) for l in input().split()]
if len(S) <= 1:
    raise Exception()
if len(C) <= 1:
    raise Exception()
INF = sum(C) + 1
# data[位置][そこが0/1] = index0から01が交互になる文字列にするコスト
data = []
for n in range(N):
    data.append([0, 0])
if S[0] == "0":
    data[0][0] = 0
    data[0][1] = C[0]
else:
    data[0][0] = C[0]
    data[0][1] = 0
for n in range(1, N):
    if S[n] == "0":
        data[n][0] = data[n-1][1]
        data[n][1] = data[n-1][0] + C[n]
    else:
        data[n][0] = data[n-1][1] + C[n]
        data[n][1] = data[n-1][0]
# それぞれに連続させる位置を総当り
result = INF
for idx in range(N - 1):
    # 00を挟む場合
    tmp = 0
    if idx > 0:
        tmp += data[idx - 1][1]
    if (N - 1 - idx) % 2:
        tmp += data[N - 1][0] - data[idx + 1][0]
    else:
        tmp += data[N - 1][1] - data[idx + 1][0]
    if S[idx] == "1":
        tmp += C[idx]
    if S[idx + 1] == "1":
        tmp += C[idx + 1]
    result = tmp if tmp < result else result
    # 11を挟む場合
    tmp = 0
    if idx > 0:
        tmp += data[idx - 1][0]
    if (N - 1 - idx) % 2:
        tmp += data[N - 1][1] - data[idx + 1][1]
    else:
        tmp += data[N - 1][0] - data[idx + 1][1]
    if S[idx] == "0":
        tmp += C[idx]
    if S[idx + 1] == "0":
        tmp += C[idx + 1]
    result = tmp if tmp < result else result
print(result)
