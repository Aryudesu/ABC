N, A, B = [int(l) for l in input().split()]
n = N // A
res = 0
if A > B:
    if N >= A:
        res = (n - 1) * B + 1
        if N % A >= B:
            res += B - 1
        else:
            res += (N % A) % B
    else:
        N = 0
else:
    if N >= A:
        res = N - A + 1
    else:
        res = 0
print(res)
