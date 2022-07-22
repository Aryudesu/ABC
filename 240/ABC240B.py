N = int(input())
A = [int(l) for l in input().split()]
d = dict()
for a in A:
    d[a] = 1
key = d.keys()
print(len(key))
