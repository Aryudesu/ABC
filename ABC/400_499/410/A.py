N = int(input())
A = [int(l) for l in input().split()]
K = int(input())
c = 0
for a in A:
    if K <= a:
        c += 1
print(c)
