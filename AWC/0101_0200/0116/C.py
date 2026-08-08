N, K = map(int, input().split())
H = list(map(int, input().split()))
data = []
down = True
idx = 0
tmp = []
for idx in range(N):
    if idx == 0:
        tmp.append(H[idx])
    elif idx == N-1:
        tmp.append(H[idx])
        data.append(tmp)
    elif H[idx] == H[idx+1]:
        tmp.append(H[idx])
        data.append(tmp)
        tmp = []
    elif H[idx-1] > H[idx] and H[idx] < H[idx+1]:
        tmp.append(H[idx])
        data.append(tmp)
        tmp = [H[idx]]
    else:
        tmp.append(H[idx])
result = 0
for dat in data:
    isOk = True
    topF = not False
    M = -1
    m = 10**10
    for idx in range(len(dat)):
        M = max(M, dat[idx])
        m = min(m, dat[idx])
        if idx + 1 < len(dat) and dat[idx] == dat[idx + 1]:
            isOk = False
            break
        # if 0 < idx and idx + 1 < len(dat) and dat[idx-1] < dat[idx] and dat[idx] > dat[idx + 1]:
        #     topF = True
    if topF and isOk and M - m >= K:
        result = max(result, len(dat))
print(result)
