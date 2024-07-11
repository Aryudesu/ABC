N = int(input())
S = input()
try:
    res = S.index("ABC")
    print(res + 1)
except:
    print(-1)
