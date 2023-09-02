def calc(N, L):
    LS = sum(L)
    for l in L:
        if LS - l <= l:
            return "No"
    return "Yes"


N = int(input())
L = [int(l) for l in input().split()]
print(calc(N, L))
