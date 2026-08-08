N, L, R = map(int, input().split())
result = 0
for n in range(N):
    T = int(input())
    result += L <= T <= R
print(result)
