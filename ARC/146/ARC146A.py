import itertools

N = int(input())
A = [l for l in input().split()]
AL = [[len(l), l] for l in A]
AL.sort(reverse=True)
R = [AL[0][1], AL[1][1], AL[2][1]]
res = 0
for l in list(itertools.permutations(R)):
    i = int(l[0] + l[1] + l[2])
    if res < i:
        res = i
print(res)
