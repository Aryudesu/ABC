N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = 1
data = dict()
count = 0
for i in range(N):
    if data.get(A[i], 0) == 0:
        if count == K:
            break
        count += 1
    result += 1
    data[A[i]] = data.get(A[i], 0) + 1
for i in range(1, N):
    data[A[i - 1]] = data.get(A[i - 1], 0) - 1
    if data.get(A[i - 1], 0) == 0:
        count -= 1
    if i + result >= N:
        break
    if count <= K:
        c = 1
        while i + result + c < N:
            idx = i + result + c
            if data.get(A[idx], 0):
                data[A[idx]] = data.get(A[idx], 0) + 1
                result += 1
            else:
                if count == K:
                    break
                data[A[idx]] = data.get(A[idx], 0) + 1
                result += 1
            c += 1
print(result)
