def calc(N, S):
    x_idx = -1
    o_idx = -1
    result = 0
    for idx in range(N):
        if S[idx] == "o":
            o_idx = idx
        elif S[idx] == "x":
            x_idx = idx
        if o_idx >= 0 and x_idx >= 0:
            if S[idx] == "o":
                result += x_idx + 1
            elif S[idx] == "x":
                result += o_idx + 1
    return result

N = int(input())
S = input()
print(calc(N, S))
