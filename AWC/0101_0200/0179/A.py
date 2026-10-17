N, X = map(int, input().split())
A = list(map(int, input().split()))
result = ["o" if a <= X else "x" for a in A]
print("".join(result))
