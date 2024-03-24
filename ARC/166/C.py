def calc(N, X, Y):
    result = True
    idx = 0
    while idx < N:
        if X[idx] != Y[idx]:
            if X[idx] == "A" and Y[idx] == "B":
                # 入れ替えられる場合入れ替える
                if idx < N - 1:
                    if X[idx + 1] == "B":
                        X[idx], X[idx + 1] = X[idx + 1], X[idx]
                else:
                    return False
            elif X[idx] == "C":
                pass
        print(X, Y)
        idx += 1
    return result


T = int(input())
result = []
for t in range(T):
    N, X, Y = [l for l in input().split()]
    result.append("Yes" if calc(int(N), list(X), list(Y)) else "No")
for r in result:
    print(r)
