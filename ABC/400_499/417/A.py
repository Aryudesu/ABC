N, A, B = [int(l) for l in input().split()]
S = input()
result = ""
for i in range(A, N-B):
    result += S[i]
print(result)
