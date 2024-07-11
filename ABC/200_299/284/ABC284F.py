N = int(input())
T = input()
for i in range(N + 1):
    if T[0] == T[N + i - 1] and T[-1] == T[i]:
        S1 = T[:i] + T[N + i:]
        S2 = T[i:N + i][::-1]
        if S1 == S2:
            print(S1)
            print(i)
            break
