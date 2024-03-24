def calc(N, S):
    for i in range(1, N):
        if S[:i] < S[i:]:
            return True
    return False


T = int(input())
result = []
for t in range(T):
    N = int(input())
    S = input()
    result.append("Yes" if calc(N, S) else "No")
for r in result:
    print(r)
