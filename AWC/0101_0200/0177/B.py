N = int(input())
S = input()
result = [False] * N
for idx in range(N):
    if S[idx] == "G":
        result[max(0, idx - 1)] = True
        result[idx] = True
        result[min(idx+1, N-1)] = True
print(N - sum(result))
