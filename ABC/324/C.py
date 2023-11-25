def calc(S, T):
    if len(S) == len(T):
        r = 0
        for idx in range(len(S)):
            if S[idx] != T[idx]:
                r += 1
        return r <= 1
    elif len(S) + 1 == len(T):
        r = 0
        for idx in range(len(S)):
            if S[idx] != T[idx + r]:
                if S[idx] != T[idx + 1]:
                    return False
                r += 1
                if r > 1:
                    return False
        return (r == 1 and S[-1] == T[-1]) or r == 0
    elif len(S) == len(T) + 1:
        r = 0
        for idx in range(len(T)):
            if S[idx + r] != T[idx]:
                if S[idx + 1] != T[idx]:
                    return False
                r += 1
                if r > 1:
                    return False
        return (r == 1 and S[-1] == T[-1]) or r == 0
    return False


N, T = [l for l in input().split()]
N = int(N)
result = []
for n in range(N):
    S = input()
    if calc(S, T):
        result.append(n + 1)

print(len(result))
print(*result)
