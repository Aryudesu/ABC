N, M = map(int, input().split())
d = 0
for n in range(N):
    a, b = map(int, input().split())
    tmp_d = (M - a)//b
    if a + b * tmp_d < M:
        tmp_d += 1
    d = max(d, tmp_d)
print(d)
