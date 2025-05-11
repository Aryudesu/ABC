from functools import lru_cache

RESULT = []

@lru_cache()
def calc(S, idx, prev, count):
    if idx == len(S) - 1:
        return True
    if count == 0:
        return True
    if prev == "o" and S[idx] == "o":
        return False
    res = False
    if S[idx] == "?":
        res1 = calc(S, idx + 1, ".", count)
        res2 = calc(S, idx + 1, "o", count - 1)
        if res1:
            RESULT[idx] |= 1
        if res2:
            RESULT[idx] |= 2
        res = res1 or res2
    else:
        res = calc(S, idx + 1, S[idx], count)
    return res

N, K = [int(l) for l in input().split()]
RESULT = [0] * N
S = input()
o_count = S.count("o")
if S[0] == ".":
    res = calc(S, 1, ".", K - o_count)
elif S[0] == "o":
    res = calc(S, 1, "o", K - o_count - 1)
elif S[0] == "?":
    res = calc(S, 1, ".", K - o_count)
    res = calc(S, 1, "o", K - o_count - 1)
print(RESULT)
