N, M, Q = map(int, input().split())
SUF = []
for n in range(N):
    s, u, f = map(int, input().split())
    SUF.append((s, u, f))

for _ in range(Q):
    d, c = input().split()
    d = int(d)
    match c:
        case "+":
            s, u, f = SUF[d-1]
            SUF[d-1] = (s + 1, 7 - f, u)
        case "-":
            s, u, f = SUF[d-1]
            SUF[d-1] = (s - 1, f, 7 - u)
for s, u, f in SUF:
    print(s, u)
