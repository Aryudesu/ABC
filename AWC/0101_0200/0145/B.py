N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
S = sum(A)
s = 0
c = 0
for a in A:
    c += 1
    s += a
    if s * 2 >= S:
        break
print(c)
