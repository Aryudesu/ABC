N = int(input())
isLogin = False
count = 0
for n in range(N):
    S = input()
    if S == "login":
        isLogin = True
    elif S == "logout":
        isLogin = False
    elif S == "public":
        pass
    elif S == "private":
        if not isLogin:
            count += 1
print(count)
