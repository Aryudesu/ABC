N = int(input())
result = 0
l, r = None, None
for n in range(N):
    a, s = [l for l in input().split()]
    a = int(a)
    if s == "L":
        if l is None:
            l = a
        else:
            result += abs(l - a)
            l = a
    if s == "R":
        if r is None:
            r = a
        else:
            result += abs(r - a)
            r = a
print(result)
