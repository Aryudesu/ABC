S = list(input())
a, b = [int(l) - 1 for l in input().split()]
S[a], S[b] = S[b], S[a]
print("".join(S))
