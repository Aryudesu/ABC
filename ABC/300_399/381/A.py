def calc(N, S):
    M = (N - 1) // 2
    SP = S.split("/")
    if len(SP) != 2:
        return False
    return SP[0] == "1" * M and SP[1] == "2" * M


N = int(input())
S = input()
print("Yes" if calc(N, S) else "No")
