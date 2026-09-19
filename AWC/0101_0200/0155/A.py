N = int(input())
result = [0] * N
target = "tanabata"
for n in range(N):
    S = input()
    count = 0
    for l in range(len(S)):
        isOk = True
        for m in range(len(target)):
            if l + m >= len(S):
                isOk = False
                break
            if S[l + m] != target[m]:
                isOk = False
                break
        count += isOk
    result[n] = count
print(result.index(max(result)) + 1)
