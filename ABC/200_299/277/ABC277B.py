N = int(input())
S = set()
for n in range(N):
    C = input()
    if C[0] in ['H', 'D', 'C', 'S'] and C[1] in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        S.add(C)
print('Yes' if len(S) == N else 'No')
