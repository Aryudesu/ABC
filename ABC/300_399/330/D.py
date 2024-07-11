N = int(input())
S = []
for n in range(N):
    S.append(input())
W = [0] * N
H = [0] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            H[i] += 1
            W[j] += 1
result = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            result += (H[i] - 1) * (W[j] - 1)
print(result)
