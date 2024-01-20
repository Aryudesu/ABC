def calc(N, A):
    lData = []
    rData = []
    lcount = 0
    rcount = 0
    for i in range(N):
        ltmp = A[i]
        if ltmp <= lcount:
            lcount = ltmp - 1
        lcount += 1
        lData.append(lcount)
        rtmp = A[- i - 1]
        if rtmp <= rcount:
            rcount = rtmp - 1
        rcount += 1
        rData.append(rcount)
    rData.reverse()
    result = 0
    for i in range(N):
        tmp = min(lData[i], rData[i])
        result = max(tmp, result)
    return result


N = int(input())
A = [int(l) for l in input().split()]
print(calc(N, A))

