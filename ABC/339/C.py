N = int(input())
A = [int(l) for l in input().split()]
m = max(A)
s = 0
for a in A:
    s += a
    if s < m:
        m = s
if m < 0:
    print(s - m)
else:
    print(s)
