N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
C = [b for b in B]
C.sort(reverse=True)
r_map = dict()
a = 0
for c in C:
    while a < N:
        if c >= A[a]:
            r_map[c] = a + 1
            break
        else:
            a += 1
for b in B:
    print(r_map.get(b, -1))
