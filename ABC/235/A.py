N = int(input())
print(N + (N % 10) * 100 + N // 10 + (N % 100) * 10 + N // 100)
