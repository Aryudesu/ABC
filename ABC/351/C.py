N = int(input())
A = [int(l) for l in input().split()]
data = []
data.append(A[0])
# 入っている個数
r = 1
for n in range(1, N):
    # print(n, data, r)
    a = A[n]
    while True:
        if data[r - 1] == a:
            a += 1
            r -= 1
            if r <= 0:
                r = 0
                data[0] = a
                r += 1
                break
        else:
            if len(data) == r:
                data.append(a)
            else:
                data[r] = a
            r += 1
            break
# print(data)
print(r)
