def calc(N, S):
    T = 0
    A = 0
    LTidx = 0
    LAidx = 0
    for idx in range(N):
        if S[idx] == "T":
            T += 1
            LTidx = idx
        elif S[idx] == "A":
            A += 1
            LAidx = idx
    if T != A:
        return "T" if T > A else "A"
    return "T" if LTidx < LAidx else "A"


N = int(input())
S = input()
print(calc(N, S))
