N, Y, M = map(int, input().split())
thisMonth = 0
nextMonth = 0
for n in range(N):
    a, b, p, q, c = map(int, input().split())
    if Y == p and M == q:
        thisMonth += c
    elif Y == p and M + 1 == q:
        nextMonth += c
    elif Y + 1 == p and M == 12 and q == 1:
        nextMonth += c        
print(thisMonth, nextMonth)
