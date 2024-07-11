import bisect

MOD = 10**8

def calcOver(N, A):
    B = [a for a in A]
    B.sort()
    result = 0
    cCount = 0
    for n in range(N):
        b = B[n]
        if b * 2 >= MOD:
            cCount += 1
        mb = MOD - b
        tmp = bisect.bisect_left(B, mb)
        result += N - tmp
    # print((result - cCount) // 2)
    return (result - cCount) // 2

N = int(input())
A = [int(l) for l in input().split()]
AllSum = sum(A) * (N - 1)
print(AllSum - MOD * calcOver(N, A))
