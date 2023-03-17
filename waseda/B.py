N = int(input())
S = input()
data = [N + 1] * N
data[0] = 0
for idx in range(N):
    tmp = data[idx]
    if S[idx] == "X":
        tmp += 1
    for j in range(1, 4):
        if idx + j >= N:
            continue
        if data[idx + j] > tmp:
            data[idx + j] = tmp
print(data[-1])
