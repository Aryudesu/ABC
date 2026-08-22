N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
I = min(B)
result = 0
c = 0
for a in A:
    if c + a <= I:
        c += a
        result += 1
print(result)
