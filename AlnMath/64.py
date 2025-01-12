def calc(N, K, A):
    s = 0
    for a in A:
        s += abs(a)
    if K < s:
        return False
    if (K - s) % 2:
        return False
    return True

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print("Yes" if calc(N, K, A) else "No")
