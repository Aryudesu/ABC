N, K = map(int, input().split())
manzoku = []
for n in range(N):
    C = int(input())
    V = list(map(int, input().split()))
    V.sort()
    m = V[(C+1)//2 - 1]
    manzoku.append(m)
manzoku.sort(reverse=True)
print(sum(m for m in manzoku[:K] if m >= 0))
