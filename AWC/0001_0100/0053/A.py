N = int(input())
A = list(map(int, input().split()))
print("Takahashi" if sum(A) % 2 else "Aoki")
