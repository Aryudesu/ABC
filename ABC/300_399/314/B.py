N = int(input())
A = []
for n in range(N):
    C = input()
    A.append({int(l) for l in input().split()})
X = int(input())
data = dict()
min = 100
for n in range(N):
    if X in A[n]:
        num = len(A[n])
        if min > num:
            min = num
        tmp = data.get(num, [])
        tmp.append(n + 1)
        data[num] = tmp
print(len(data.get(min, [])))
print(*data.get(min, []))
