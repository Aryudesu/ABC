ALP = dict()
S = "abcdefghijklmnopqrstuvwxyz"
for idx in range(len(S)):
    ALP[S[idx]] = idx

def calc(W: str, K: int)->str:
    ini = 0
    for w in W:
        ini += ALP[w] + 1
    result = []
    if ini % 2:
        if K % 2:
            result = list(W)
            result.reverse()
            return "".join(result)
        return W
    if len(W) % 2:
        for c in W:
            idx = ALP[c]
            result.append(S[(idx + 1) % len(S)])
        if (K - 1) % 2:
            result.reverse()
        return "".join(result)

    for c in W:
        idx = ALP[c]
        result.append(S[(idx + K) % len(S)])
    return "".join(result)
    


N, K = map(int, input().split())
for n in range(N):
    W = input()
    print(calc(W, K))

