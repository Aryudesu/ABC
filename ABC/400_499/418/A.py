N = int(input())
S = input()
if N < 3:
    print("No")
else:
    print("Yes" if S[-3:] == "tea" else "No")
