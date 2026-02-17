N = int(input())
S = []
m = 0
for _ in range(N):
    s = input()
    m = max(m, len(s))
    S.append(s)
for n in range(N):
    s = S[n]
    k = (m - len(s))//2
    print(f"{'.' * k}{s}{'.' * k}")
