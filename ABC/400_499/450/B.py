def calc(N: int, C: list[list[int]]):
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if not (a < b < c):
                    continue
                ac = C[a][c-a-1]
                ab = C[a][b-a-1]
                bc = C[b][c-b-1]
                # print(a, b, c)
                # print(ac, ab, bc)
                if ac > ab + bc:
                    return True
                # print(a, b, c, ac, ab, bc)
    return False

N = int(input())
C = []
for n in range(N-1):
    c = list(map(int, input().split()))
    C.append(c)
res = calc(N, C)
print("Yes" if res else "No")
