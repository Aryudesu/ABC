from sortedcontainers import SortedList

N = int(input())
LH = []
data = SortedList()
for n in range(N):
    h, l = map(int, input().split())
    LH.append((l, h))
    data.add(h)
LH.sort(reverse=True)
Q = int(input())
T = list(map(int, input().split()))
query = []
for q in range(Q):
    query.append((T[q], q))
query.sort(reverse=True)

result = [None] * Q
while query:
    t, q = query.pop()
    while LH:
        l, h = LH.pop()
        if l > t:
            LH.append((l, h))
            break
        data.discard(h)
    result[q] = data[-1]
for r in result:
    print(r)
