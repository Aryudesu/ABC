N = int(input())
S = []
for _ in range(N):
    m, *s = list(map(int, input().split()))
    S.append(s)
failed = 0
Q = int(input())
for _ in range(Q):
    v, d = map(int, input().split())
    if S[v-1][d-1] > 0:
        S[v-1][d-1] -= 1
    else:
        failed +=1
for s in S:
    print(*s)
print(failed)
