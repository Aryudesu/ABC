def isMatch(N: int, S: str, T: str)->bool:
    for idx in range(N):
        if T[idx] == "*":
            continue
        if S[idx] != T[idx]:
            return False
    return True

N = int(input())
S = input()
T = input()
print("Yes" if isMatch(N, S, T) else "No")
