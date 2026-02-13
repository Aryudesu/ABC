N = int(input())
H = list(map(int, input().split()))
H.sort()
result1 = abs(H[0])
for i in range(N-1):
    result1 += abs(H[i+1] - H[i])
result1 += abs(H[-1])
H.reverse()
result2 = abs(H[0])
for i in range(N-1):
    result2 += abs(H[i+1] - H[i])
result2 += abs(H[-1])
print(min(result1, result2))
