N = int(input())
A = [int(l) for l in input().split()]
M = int(input())
B = [int(l) for l in input().split()]
L = int(input())
C = [int(l) for l in input().split()]
Q = int(input())
X = [int(l) for l in input().split()]
memo = set()
for a in A:
    for b in B:
        for c in C:
            memo.add(a + b + c)
result = []
for x in X:
    if x in memo:
        result.append("Yes")
    else:
        result.append("No")
for r in result:
    print(r)
