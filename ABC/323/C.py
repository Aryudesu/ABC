N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [[A[i], i]for i in range(M)]
B.sort(reverse=True)
mP = 0
mPC = 0
person = [0] * N
S = []
for n in range(N):
    s = input()
    S.append(s)
    for m in range(M):
        tmp = B[m][1]
        if S[n][tmp] == "o":
            person[n] += B[m][0]
    person[n] += n + 1
    if mP < person[n]:
        mP = person[n]
        mPC = 1
    elif mP == person[n]:
        mPC += 1
result = []
for n in range(N):
    # プレイヤーn-1の点数
    tmp = person[n]
    # 唯一の最高得点の場合
    if mP == tmp and mPC == 1:
        result.append(0)
    else:
        count = 0
        for m in range(M):
            if S[n][B[m][1]] != "o":
                tmp += B[m][0]
                count += 1
                if tmp > mP:
                    result.append(count)
                    break
for r in result:
    print(r)
