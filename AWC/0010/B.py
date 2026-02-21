N = int(input())
D = list(map(int, input().split()))
result = 0
result += D[0]
for i in range(1, N):
    if D[i] > D[i-1]:
        result += D[i]//2
    else:
        result += D[i]
print(result)
