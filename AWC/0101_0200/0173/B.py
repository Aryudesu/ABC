H, W = map(int, input().split())
data = [set() for _ in range(W)]
for h in range(H):
    S = input()
    for w in range(W):
        data[w].add(S[w])
print(sum(len(data[w]) == 1 and "." in data[w] for w in range(W)))
