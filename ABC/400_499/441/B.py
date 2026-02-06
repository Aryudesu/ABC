def calc(S: set[str], T: set[str], W: str)-> str:
    isTakahashi = True
    isAoki = True
    for w in W:
        if not w in S:
            isTakahashi = False
        if not w in T:
            isAoki = False
    if isTakahashi and isAoki:
        return "Unknown"
    elif isTakahashi:
        return "Takahashi"
    elif isAoki:
        return "Aoki"
    else:
        raise Exception()

N, M = map(int, input().split())
S = set(list(input()))
T = set(list(input()))
result = []
Q = int(input())
for _ in range(Q):
    w = input()
    result.append(calc(S, T, w))
for r in result:
    print(r)
