N, M, D, K = map(int, input().split())
A = [max(0, int(l) - M * D) for l in input().split()]
A.sort()
for k in range(min(K, M)):
    if not A:
        break
    A.pop()
if not A:
    print(0)
else:
    print(sum(a > 0 for a in A))
