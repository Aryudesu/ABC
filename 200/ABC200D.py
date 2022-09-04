N = int(input())
A = [int(l) % 200 for l in input().split()]
A8 = []
AS = set()
for a in A:
    if a not in AS:
        A8.append(a)
    AS.add(a)

L = len(A8)
data = dict()
for idx in range(2 ** L):
    tmp = 0
    n = idx
    tmp = 0
    while True:
        tmp += A8[tmp]
