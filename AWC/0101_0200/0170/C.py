def calc(A: list[int], M: int)->set[int]:
    dp = {0}
    for a in A:
        nextDP = dp.copy()
        for num in dp:
            if num + a == M:
                return M
            elif num + a <= M:
                nextDP.add(num + a)
        dp = nextDP
    return max(dp)

N = int(input())
A = list(map(int, input().split()))
S = sum(A)
L = (S + 1) // 2
res = calc(A, L)
print(abs(res - (S-res)))
