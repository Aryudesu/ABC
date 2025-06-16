def makeIdx(N, S):
    l = -1
    r = -1
    for idx in range(N-1):
        if l >= 0 and r < 0 and S[l] < S[idx + 1]:
            r = idx
        if l < 0 and r < 0 and S[idx] > S[idx + 1]:
            l = idx
    if l >= 0 and r < 0:
        r = N - 1
    return l, r

def calc(N, S):
    lidx, ridx = makeIdx(N, S)
    # print(lidx, ridx)
    if lidx < 0:
        print(S)
        return
    for i in range(N):
        if i < lidx:
            print(S[i], end="")
        elif i < ridx:
            print(S[i + 1], end="")
        elif i == ridx:
            print(S[lidx], end = "")
        else:
            print(S[i], end = "")
    print()


T = int(input())
for t in range(T):
    N = int(input())
    S = input()
    calc(N, S)
