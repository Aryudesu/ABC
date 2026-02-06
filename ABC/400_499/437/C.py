def calc(N, WP):
    allW = 0
    data = []
    for w, p in WP:
        allW += w
        data.append(p+w)
    data.sort(reverse=True)
    count = 0
    cost = 0
    for d in data:
        count += 1
        cost += d
        if cost >= allW:
            return N - count
    

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    WP = []
    for n in range(N):
        w, p = map(int, input().split())
        WP.append((w, p))
    result.append(calc(N, WP))
for r in result:
    print(r)
