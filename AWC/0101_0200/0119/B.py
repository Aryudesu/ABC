N = int(input())
B = list(map(int, input().split()))
S = sum(B)
result = 0
for n in range(N-1):
    result += S
    S -= B[n]
print(result)
