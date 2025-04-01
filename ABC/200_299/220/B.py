K = int(input())
Astr, Bstr = [l for l in input().split()]
A = 0
for a in Astr:
    A = A * K + int(a)
B = 0
for b in Bstr:
    B = B * K + int(b)
print(A * B)
