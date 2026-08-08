N, Q = map(int, input().split())
S = list(input())
data = [False]
for i in range(1, N):
    data.append(S[i-1] == S[i])
result = []
M = sum(data)
# print("debug", M)
# print(data)
for _ in range(Q):
    i, c = input().split()
    i = int(i) - 1
    if S[i] != c:
        if i - 1 >= 0:
            if S[i - 1] == c:
                if not data[i]:
                    data[i] = True
                    M += 1
            else:
                if data[i]:
                    data[i] = False
                    M -= 1
        if i + 1 < N:
            if S[i + 1] == c:
                if not data[i + 1]:
                    data[i + 1] = True
                    M += 1
            else:
                if data[i + 1]:
                    data[i + 1] = False
                    M -= 1
    S[i] = c
    # print(S)
    # print(data)
    result.append(M)
print(*result, sep="\n")
