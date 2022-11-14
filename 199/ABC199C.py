N = int(input())
S = list(input())
Q = int(input())
is_return = False
for q in range(Q):
    T, A, B = [int(l) for l in input().split()]
    A = A - 1
    B = B - 1
    if T == 2:
        is_return = not is_return
    else:
        new_A = A
        new_B = B
        if A >= N and is_return:
            new_A = A - N
        elif A < N and is_return:
            new_A = A + N
        if B >= N and is_return:
            new_B = B - N
        elif B < N and is_return:
            new_B = B + N
        t = S[new_A]
        S[new_A] = S[new_B]
        S[new_B] = t
    # print(S)
result = S[N:] + S[:N] if is_return else S
print("".join(result))
