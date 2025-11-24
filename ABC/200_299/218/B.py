alp = "abcdefghijklmnopqrstuvwxyz"
P = list(map(int, input().split()))
result = [alp[i-1] for i in P]
print("".join(result))
