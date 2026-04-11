N, M = map(int, input().split())
C = list(map(int, input().split()))
counter = [0] * (N + 1)
for m in range(M):
    t = int(input())
    if counter[t] < C[t-1]:
        counter[t] += 1
print(sum(counter))
