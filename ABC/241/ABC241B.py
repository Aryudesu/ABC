def eatPasta(A, B):
    for day in B:
        if day in A:
            i = A.index(day)
            A.pop(i)
        else:
            return "No"
    return "Yes"


N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
print(eatPasta(A, B))
