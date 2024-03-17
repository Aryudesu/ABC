N = int(input())
S = input()
Q = int(input())
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
ALP = dict()
for a in Alphabet:
    ALP[a] = a
memo = dict()
for a in Alphabet:
    memo[a] = False
def change(c, d):
    for k in ALP:
        if ALP[k] == c:
            ALP[k] = d
for _ in range(Q):
    C, D = [l for l in input().split()]
    change(C, D)
result = []
for s in S:
    result.append(ALP[s])
print("".join(result))
