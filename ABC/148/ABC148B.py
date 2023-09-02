N = int(input())
S, T = [l for l in input().split()]
result = [S[idx] + T[idx] for idx in range(N)]
print("".join(result))
