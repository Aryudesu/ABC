def calc(S, A):
    dp = set()
    dp.add(0)
    for a in A:
        new_dp = set()
        for n in dp:
            new_dp.add(n)
            if n + a == S:
                return True
            if n + a <= S:
                new_dp.add(n + a)
        dp = new_dp
    return False


N, S = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print("Yes" if calc(S, A) else "No")
