N = int(input())
data11 = [0] * (N+1)
data01 = [0] * (N+1)
data10 = [0] * (N+1)
data11[0] = 1
for i in range(1, N+1):
    data11[i] += data11[i-1]
    if i >= 2:
        data11[i] += data11[i-2] + data01[i-1] + data10[i-1]
        data01[i] += data11[i-2] + data10[i-1]
        data10[i] += data11[i-2] + data01[i-1]
print(data11[-1])
