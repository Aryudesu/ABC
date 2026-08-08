N, M = map(int, input().split())
EC = []
for n in range(N):
    e, c = map(int, input().split())
    EC.append((e, c))
EC.sort()
D = list(map(int, input().split()))
D.sort(reverse=True)
result = 0
for e, c in EC:
    while c > 0 and D and D[-1] <= e:
        D.pop()
        result += 1
        c -= 1
        # print(e, c, D)
print(result)
