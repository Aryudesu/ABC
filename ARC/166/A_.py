def calc(N, X, Y):
    XA = 0
    YA = 0
    for n in range(N):
        if X[n] == "A":
            XA += 1
        if Y[n] == "A":
            YA += 1
    dp = set()
    dp.add(0)
    for n in range(N):
        new_dp = set()
        # YはCで仕切りが作られる
        if Y[n] == "C" and X[n] != "C":
            return False
        elif Y[n] == "C" and X[n] == "C":
            # Aの数が合わなければダメ
            if not 0 in dp:
                return False
            dp = set()
            dp.add(0)
            continue
        for d in dp:
            if X[n] == "A":
                if Y[n] == "A":
                    new_dp.add(d)
                else:
                    new_dp.add(d + 1)
            elif X[n] == "B":
                if Y[n] == "A" and d > 0:
                    new_dp.add(d - 1)
                else:
                    new_dp.add(d)
            elif X[n] == "C":
                if Y[n] == "A" and d > 0:
                    new_dp.add(d - 1)
                elif YA > d:
                    new_dp.add(d + 1)
                new_dp.add(d)
        dp = new_dp
        # print(dp)
    return 0 in dp


T = int(input())
result = []
for t in range(T):
    N, X, Y = [l for l in input().split()]
    result.append("Yes" if calc(int(N), list(X), list(Y)) else "No")
for r in result:
    print(r)
