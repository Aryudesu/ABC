N, T, P = [int(l) for l in input().split()]
L = [int(l) for l in input().split()]
L.sort(reverse=True)
if L[P - 1] >= T:
    print(0)
else:
    print(T - L[P - 1])
