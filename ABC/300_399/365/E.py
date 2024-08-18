N = int(input())
A = [int(l) for l in input().split()]
AL = []
AR = []
s = 0
for a in A:
    s ^= a
    AL.append(s)
s = 0
for i in range(N - 1, -1, -1):
    a = A[i]
    s ^= a
    AR.append(s)
AR.reverse()
print(AL, AR)
