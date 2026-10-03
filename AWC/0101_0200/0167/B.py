N = int(input())
A = list(map(int, input().split()))
print("Yes" if A.count(1) >= 2 or 0 in A else "No")
