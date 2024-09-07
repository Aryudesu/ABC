N = int(input())
A = [int(l) for l in input().split()]
data = []
for i in range(N - 1):
    data.append(A[i + 1] - A[i])
result = 0
memo = None
count = 0
for i in range(N - 1):
    dat = data[i]
    if memo is None:
        memo = dat
        count = 1
    elif memo == dat:
        count += 1
    elif memo != dat:
        result += ((count + 1) * count) // 2
        memo = dat
        count = 1
        # print("test", count, ((count + 1) * count) // 2)
    # print(count, memo, result)
result += ((count + 1) * count) // 2
print(result + N)
