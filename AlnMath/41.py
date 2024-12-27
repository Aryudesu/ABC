T = int(input())
data = [0] * (T + 1)
N = int(input())
for n in range(N):
    l, r = [int(l) for l in input().split()]
    data[l] += 1
    data[r] -= 1
result = 0
for t in range(T):
    result += data[t]
    print(result)
