N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
MOD = 10**9 + 7
dp = {0: 1}
for a in A:
    new_dp = set()
    for d in dp:
        for c in range(a + 1):
            pass
