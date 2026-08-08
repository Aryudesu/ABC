def calc(N: int, P: list[int], Q: list[int])->bool:
    pIdx = dict()
    for idx in range(N):
        p = P[idx]
        pIdx[p] = idx
    data = []
    for idx in range(N):
        q = Q[idx]
        data.append(pIdx[q])
    tenho = True
    for idx in range(N):
        if data[idx] != idx:
            tenho = False
            break
    if tenho:
        return True

    l = 0
    for idx in range(N):
        if idx != data[idx]:
            l = idx
            break
    r = N-1
    for idx in range(N-1, -1, -1):
        if idx != data[idx]:
            r = idx
            break
    L = data[:l]
    M = data[l:r+1]
    R = data[r+1:]
    M.reverse()
    newData = L + M + R
    for idx in range(N):
        if newData[idx] != idx:
            return False
    return True

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
print("Yes" if calc(N, P, Q) else "No")
