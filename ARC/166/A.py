def calc(N, X, Y):
    idx = 0
    while idx < N:
        if X[idx] != Y[idx]:
            if X[idx] == "A" and Y[idx] == "B":
                # 入れ替えられる場合入れ替える
                if idx < N - 1:
                    if X[idx + 1] == "B":
                        X[idx], X[idx + 1] = X[idx + 1], X[idx]
                    elif X[idx + 1] == "C":
                        X[idx], X[idx + 1] = "B", "A"
                else:
                    return False
            elif X[idx] == "B" and Y[idx] != "B":
                return False
            elif X[idx] == "C":
                if Y[idx] == "A":
                    X[idx] = "A"
                elif Y[idx] == "B":
                    if idx < N - 1:
                        if X[idx + 1] == "B" and Y[idx + 1] == "A":
                            X[idx], X[idx + 1] = "B", "A"
                        else:
                            X[idx] = "B"
                    else:
                        return True
                elif Y[idx] == "C":
                    pass
                elif idx == N - 1:
                    return True
        print(X, Y)
        idx += 1
    return True


T = int(input())
result = []
for t in range(T):
    N, X, Y = [l for l in input().split()]
    result.append("Yes" if calc(int(N), list(X), list(Y)) else "No")
for r in result:
    print(r)
