N = int(input())
result = [False] * N
for n in range(N):
    s, k = input().split()
    k = int(k)
    result[n] = s == "Yes"
    if k % 2:
        result[n] = not result[n]
for r in result:
    print("Yes" if r else "No")
