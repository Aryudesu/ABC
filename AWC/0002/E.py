from itertools import product

N, S = map(int, input().split())
A = list(map(int, input().split()))
data1 = dict()
num1 = N // 2
for dat in product([0, 1], repeat=num1):
    tmp = 0
    for i in range(num1):
        if dat[i] == 1:
            tmp += A[i]
    data1[tmp] = data1.get(tmp, 0) + 1
data2 = dict()
num2 = N - num1
for dat in product([0, 1], repeat=num2):
    tmp = 0
    for i in range(num2):
        if dat[i] == 1:
            tmp += A[num1 + i]
    data2[tmp] = data2.get(tmp, 0) + 1
result = 0
for k in data1:
    result += data2.get(S-k, 0) * data1[k]
print(result)
