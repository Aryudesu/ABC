N, K = map(int, input().split())
A = list(map(int, input().split()))
person = []
for i in range(N):
    person.append((A[i], i))
person.sort()
result = [K//N] * N
K = K%N
for n, idx in person:
    if K == 0:
        break
    result[idx] += 1
    K-=1
for r in result:
    print(r)
