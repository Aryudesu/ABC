N, K = map(int, input().split())
print(sum(1 if input().count("!") >= K else 0 for n in range(N)))
