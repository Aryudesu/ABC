def s2i(S: str)->int:
    result = 0
    for s in S:
        result = result * 2 + int(s)
    return result

N, L, Q = map(int, input().split())
S = [s2i(input()) for _ in range(N)]
result = []
for _ in range(Q):
    res = 0
    M, *C = map(int, input().split())
    for c in C:
        res |= S[c-1]
    result.append(res)
for r in result:
    print(bin(r)[2:].zfill(L))
