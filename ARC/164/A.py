def calc(N, K):
    num = N
    s = 0
    while num:
        s += num % 3
        num //= 3
        if K < s:
            return False
    return (K - s) % 2 == 0


T = int(input())
result = []
for _ in range(T):
    N, K = [int(l) for l in input().split()]
    result.append("Yes" if calc(N, K) else "No")
for r in result:
    print(r)
