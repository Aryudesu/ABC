def isIn(target: str, S: str)->bool:
    K = len(S)
    idx = 0
    for t in target:
        while S[idx] != t:
            idx += 1
            if idx == K:
                return False
    return True

N = int(input())
S = [input() for _ in range(N)]
target = "sayounara"
for s in S:
    print("Yes" if isIn(target, s) else "No")
