def calc(N, P, Q, R, AS, AD):
    for n in range(N):
        r = AS[-n - 1] - R
        if AD.get(r, False):
            q = r - Q
            if AD.get(q, False):
                p = q - P
                if AD.get(p, False):
                    return True
    return False


N, P, Q, R = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
AS = []
AD = dict()
S = 0
for a in A:
    S += a
    AS.append(S)
    AD[S] = True
AD[0] = True
print('Yes' if calc(N, P, Q, R, AS, AD) else 'No')
