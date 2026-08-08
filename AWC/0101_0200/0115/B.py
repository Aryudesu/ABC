N, K = map(int, input().split())
A = list(map(int, input().split()))
print(sum([a <= K for a in A]))
