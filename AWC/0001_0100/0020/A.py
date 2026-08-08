N = int(input())
A = list(map(int, input().split()))
print("Yes" if sum(A) % N == 0 else "No")
