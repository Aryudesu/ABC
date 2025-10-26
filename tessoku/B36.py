N, K = map(int, input().split())
print("Yes" if (input().count("1") - K)%2 == 0 else "No")
