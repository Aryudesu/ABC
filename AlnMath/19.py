input()
A = [int(l) for l in input().split()]
data = dict()
for a in A:
    data[a] = data.get(a, 0) + 1
R = data.get(1, 0)
Y = data.get(2, 0)
B = data.get(3, 0)
print((R * (R - 1))//2 + (Y * (Y-1))//2 + (B * (B-1))//2)
