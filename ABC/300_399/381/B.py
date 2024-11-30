def calc(S):
    memo = set()
    if len(S) % 2:
        return False

    for i in range(len(S) // 2):
        if S[2 * i] != S[2 * i + 1]:
            return False
        if S[2 * i] in memo:
            return False
        memo.add(S[2 * i])
    return True

S = input()
print("Yes" if calc(S) else "No")
