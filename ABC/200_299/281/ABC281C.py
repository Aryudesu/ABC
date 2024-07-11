N, T = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
sumA = sum(A)
TA = T % sumA
s = 0
for idx in range(N):
    if TA >= s and TA < s + A[idx]:
        print(idx + 1, TA - s)
        break
    s += A[idx]
