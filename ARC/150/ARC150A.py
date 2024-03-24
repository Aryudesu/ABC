T = int(input())
res = []
for t in range(T):
    N, K = [int(l) for l in input().split()]
    S = input()
    zero = 0
    one = 0
    f = False
    for k in range(K):
        if S[k] == '?' or S[k] == '1':
            one += 1
        else:
            zero += 1
    if S[0] == '0':
        zero += 1
    elif S[0] == '?':
        one += 1
    if S[K - 1] == '0':
        zero -= 1
    elif S[K-1] == '?':
        one -= 1
    for n in range(N - K + 1):
        if S[n] == '0':
            zero -= 1
        elif S[n] == '?':
            one -= 1
        if S[n + K - 1] == '0':
            zero += 1
        else:
            one += 1
        if zero == 0:
            if f:
                f = False
                break
            f = True
    if f:
        res.append('Yes')
    else:
        res.append('No')
for r in res:
    print(r)
