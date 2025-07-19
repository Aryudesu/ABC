N = int(input())
S = []
for n in range(N):
    S.append(input())
data = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        data.add(S[i] + S[j])
print(len(data))
