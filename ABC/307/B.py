def check(S):
    tmp = list(S)
    tmp.reverse()
    return S == "".join(tmp)


def calc():
    N = int(input())
    S = []
    for n in range(N):
        S.append(input())

    for i in range(N):
        for j in range(N):
            if i != j:
                if check(S[i] + S[j]):
                    return True
    return False


print("Yes" if calc() else "No")
