N = int(input())
A = [int(l) for l in input().split()]
S = set()
count = [0] * 200
for n in range(N):
    S.add(A[n] % 200)
    count[A[n] % 200] += 1
res = 0
for s in S:
    res += count[s] * (count[s] - 1)//2
print(res)
