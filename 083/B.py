N, A, B = [int(l) for l in input().split()]
print(sum([(n+1 if A <= sum([int(l) for l in str(n+1)]) <= B else 0) for n in range(N)]))
