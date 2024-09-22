S = input()
T = input()
N = len(S)
data = []
for i in range(N):
    if S[i] == T[i]:
        data.append(0)
    elif S[i] < T[i]:
        data.append(-1)
    else:
        data.append(1)
X = []
for i in range(N):
    if data[i] == 1:
        S = S[:i] + T[i] + S[i+1:]
        X.append(S)
for i in range(N):
    j = N-i-1
    if data[j] == -1:
        S = S[:j] + T[j] + S[j+1:]
        X.append(S)
print(len(X))
for x in X:
    print(x)
