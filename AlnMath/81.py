N = int(input())//1000
print((N//10) + (1 if N%10 >= 5 else 0) + N % 5)
