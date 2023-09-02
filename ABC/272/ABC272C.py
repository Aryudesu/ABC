N = int(input())
A = [int(l) for l in input().split()]
even = []
odd = []
for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
even.sort()
odd.sort()
e, o = -1, -1
# print(even, odd)
if len(even) >= 2:
    e = even[-1] + even[-2]
if len(odd) >= 2:
    o = odd[-1] + odd[-2]
# print(e, o)
if e == -1 and o == -1:
    print(-1)
elif e > o:
    print(e)
else:
    print(o)
