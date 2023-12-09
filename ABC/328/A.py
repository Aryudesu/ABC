N, X = [int(l) for l in input().split()]
S = [int(l) if int(l) <= X else 0 for l in input().split()]
print(sum(S))
