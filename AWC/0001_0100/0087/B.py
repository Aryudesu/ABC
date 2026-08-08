N = int(input())
R = []
result = 0
for n in range(N):
    t, r = map(int, input().split())
    result += t
    result += r
    R.append(r)
print(result - max(R))

