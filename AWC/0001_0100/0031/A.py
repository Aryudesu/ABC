N, M, K = map(int, input().split())
chef = []
for n in range(N):
    vct = list(map(int, input().split()))
    v = vct[0]
    c = vct[1]
    t = vct[2:]
    chef.append((v, -n, c, t))
chef.sort(reverse=True)
result = set(chef[0][3])
for k in range(K):
    v, n, c, t = chef[k]
    result = result & set(t)
print(len(result))
