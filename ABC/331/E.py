N, M, L = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
NA = []
for n in range(N):
    NA.append((A[n], n))
NA.sort(reverse=True)
NB = []
for m in range(M):
    NB.append((B[m], m))
NB.sort(reverse=True)
data = set()
for l in range(L):
    c, d = [int(l) for l in input().split()]
    data.add((c-1, d-1))

result = 0
for na in NA:
    for nb in NB:
        tmp = (na[1], nb[1])
        if tmp not in data:
            r = na[0] + nb[0]
            if r > result:
                result = r
            break
print(result)
