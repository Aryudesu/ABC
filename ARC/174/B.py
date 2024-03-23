def calcStar(A):
    return 1 * A[0] + 2 * A[1] + 3 * A[2] + 4 * A[3] + 5 * A[4]

def calc(A, P):
    S = calcStar(A)
    N = sum(A)
    U = 3 * N - S
    if U <= 0:
        return 0
    if P[4] >= 2 * P[3]:
        n = U
        return n * P[3]
    else:
        n = U // 2
        m = U % 2
        res = n * P[4]
        if m:
            if P[4] >= P[3]:
                res += P[3]
            else:
                res += P[4]
        return res

T = int(input())
result = []
for t in range(T):
    A = [int(l) for l in input().split()]
    P = [int(l) for l in input().split()]
    result.append(calc(A, P))

for r in result:
    print(r)
