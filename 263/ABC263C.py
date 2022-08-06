N, M = [int(l) for l in input().split()]
base = [i+1 for i in range(N)]
tmp = [0 for i in range(N)]
tmp[-1] = -1
ff = False
if N == M:
    print(' '.join([str(i+1) for i in range(N)]))
elif N > M:
    pass
else:
    while True:
        if tmp[0] == M-N:
            break
        tmp[-1] += 1
        if tmp[-1] > M - N:
            idx = N-1
            f = False
            for n in range(N):
                if tmp[N-n-1] < M-N:
                    tmp[N-n-1] += 1
                    for m in range(N-n-1,N):
                        tmp[m] = tmp[N-n-1]
                    f = True
                    break
                if f:
                    break
        res = [str(base[i] + tmp[i]) for i in range(N)]
        print(' '.join(res))
