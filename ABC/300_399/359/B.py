N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for i in range(len(A)):
    a = A[i]
    if not a in data:
        data[a] = i
    else:
        data[a] -= i
# print(data)
result = 0
for a in data:
    if abs(data[a]) == 2:
        result += 1
print(result)
