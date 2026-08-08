N, K, P = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
c = 0
while H:
    if H[-1] < 0:
        tmp = (-H[-1] + P - 1) // P
        if tmp * P + H[-1] == 0:
            tmp += 1
        if c + tmp > K:
            break
        c += tmp
    elif H[-1] == 0:
        if c + 1 > K:
            break
        c += 1
    H.pop()
print(len(H))
