N, Q = [int(l) for l in input().split()]
S = list(input())
now_index = set()
for n in range(N - 2):
    if S[n] == "A" and S[n + 1] == "B" and S[n + 2] == "C":
        now_index.add(n)
result = []
for q in range(Q):
    x, c = [l for l in input().split()]
    x = int(x) - 1
    S[x] = c
    l = max([0, x - 2])
    r = min([x + 1, N - 2])
    for i in range(l, r):
        if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
            now_index.add(i)
        else:
            now_index.discard(i)
    # print(now_index)
    result.append(len(now_index))
for r in result:
    print(r)
