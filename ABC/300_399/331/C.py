N = int(input())
A = [int(l) for l in input().split()]
B = [a for a in A]
A.sort(reverse=True)
data = dict()
s = 0
M = A[0] + 1
for a in A:
    if M > a:
        M = a
        data[M] = s
        s += a
    else:
        s += a
# print(data)
result = []
for b in B:
    result.append(data.get(b, 0))
print(*result)
