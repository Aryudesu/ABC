def calc(data, N):
    for i in range(N - 1):
        for j in range(i + 1, N):
            f, s = True, True
            f1, s1 = data[i]
            f2, s2 = data[j]
            if f1 == f2 or f1 == s2:
                f = False
            if s1 == f2 or s1 == s2:
                s = False
            if not f and not s:
                return "No"
    return "Yes"


N = int(input())
data = []
for _ in range(N):
    s, t = [l for l in input().split()]
    data.append([s, t])

print(calc(data, N))
