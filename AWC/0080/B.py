N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
result = []
for _ in range(Q):
    t = int(input())
    res = 0
    while A:
        a = A.pop()
        if a >= t:
            A.append(a)
            break
        res += 1
    result.append(res)
for r in result:
    print(r)
