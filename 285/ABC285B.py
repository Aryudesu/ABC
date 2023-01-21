def calc(S, i, N):
    for k in range(1, N):
        if k + i <= N:
            if S[k - 1] == S[k + i - 1]:
                # print("A")
                return k - 1
        else:
            # print("B")
            return k - 1
    # print("C")
    return k


N = int(input())
S = input()
for i in range(1, N):
    res = 0
    print(calc(S, i, N))
