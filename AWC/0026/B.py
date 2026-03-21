N, K = map(int, input().split())
A = list(map(int, input().split()))
takahashi = 0
aoki = 0
for a in A:
    if takahashi + a <= K:
        takahashi += a
    else:
        aoki += a
# print(takahashi, aoki)
if takahashi == aoki:
    print("Draw")
elif takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    raise ValueError()
