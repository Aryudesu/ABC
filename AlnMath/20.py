N = int(input())
A = [int(l) for l in input().split()]
data = set(A)
result = 0
for ia in range(N-5+1):
    a = A[ia]
    for ib in range(ia+1, N-4+1):
        b = A[ib]
        for ic in range(ib+1, N-3+1):
            c = A[ic]
            for id in range(ic+1, N-2+1):
                d = A[id]
                for ie in range(id+1, N):
                    e = A[ie]
                    if a + b + c + d + e == 1000:
                        result += 1
print(result)
