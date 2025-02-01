VAL = 0
N = int(input())
A = [int(l) for l in input().split()]
S = [0] * N
MEMO = set()

def calc(idx, sz):
    global VAL
    for i in range(sz + 1):
        VAL ^= S[i]
        S[i] += A[idx]
        VAL ^= S[i]
        if idx == N - 1:
            MEMO.add(VAL)
        elif i < sz:
            calc(idx + 1, sz)
        else:
            calc(idx + 1, sz + 1)
        VAL^= S[i]
        S[i] -= A[idx]
        VAL ^= S[i]

calc(0, 0)
print(len(MEMO))
