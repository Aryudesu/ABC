N = int(input())
A = [int(l) for l in input().split()]
data = [0]
for a in A:
    data.append(data[-1] + a)
M = int(input())
result = 0
p = int(input()) - 1
for m in range(M - 1):
    new_p = int(input()) - 1
    result += abs(data[p] - data[new_p])
    p = new_p
print(result)
