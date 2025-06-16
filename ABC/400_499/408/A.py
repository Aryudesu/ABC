def calc(N, S, T):
    for n in range(1, N + 1):
        t = T[n] - T[n-1]
        if S < t:
            return False
    return True

N, S = [int(l) for l in input().split()]
T = [int(l) for l in ("0 " + input()).split()]
print("Yes" if calc(N, S, T) else "No")
