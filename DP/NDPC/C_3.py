from collections import defaultdict

MOD = 998244353

N = int(input())
S = input().split()
L = [len(s) for s in S]

dp = defaultdict(int)
dp[(0, 0, 0)] = 1

for _ in range(N):
    ndp = defaultdict(int)

    for state, val in dp.items():
        for x in range(26):
            ch = chr(ord("a") + x)
            ns = list(state)

            ok = True
            for i in range(3):
                if ns[i] < L[i] and S[i][ns[i]] == ch:
                    ns[i] += 1

                if ns[i] == L[i]:
                    ok = False
                    break

            if ok:
                ndp[tuple(ns)] = (ndp[tuple(ns)] + val) % MOD

    dp = ndp

print(sum(dp.values()) % MOD)
