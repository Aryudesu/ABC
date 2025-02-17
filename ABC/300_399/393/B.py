S = input()
N = len(S)
result = 0
# 先頭
for i in range(N):
    #何文字飛ばすか
    for j in range(N):
        if i + j + j >= N:
            break
        if S[i] == "A" and S[i + j] == "B" and S[i + j + j] == "C":
            result += 1
print(result)
