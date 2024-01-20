def calc(S, T):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = Alphabet.lower()
    L = len(alphabet)
    data = dict()
    for i in range(L):
        data[alphabet[i]] = i
    num = (data[S[0]] - data[T[0]]) % L
    for i in range(len(S)):
        if num != (data[S[i]] - data[T[i]]) % L:
            return False
    return True

S = input()
T = input()
print("Yes" if calc(S, T) else "No")
