from functools import lru_cache

# import pypyjit

# pypyjit.set_param('max_unroll_recursion=-1')

MAX = 10 ** 18
Data = set()
@lru_cache(maxsize=1000)
def minMax(cards, turn, alpha, beta):
    if turn:
        maxScore = alpha
        pf = False
        for dat in Data:
            if dat & cards == 0:
                pf = True
                score = minMax(cards | dat, not turn, maxScore, beta)
                if score > maxScore:
                    maxScore = score
                if maxScore >= beta:
                    return maxScore
        if not pf:
            return -1
        return maxScore
    else:
        minScore = beta
        pf = False
        for dat in Data:
            if dat & cards == 0:
                pf = True
                score = minMax(cards | dat, not turn, alpha, minScore)
                if score < minScore:
                    minScore = score
                if alpha >= minScore:
                    return minScore
        if not pf:
            return 1
        return minScore

N = int(input())
AB = []
for n in range(N):
    a, b = [int(l) for l in input().split()]
    AB.append([a, b])
AB.sort()
memo = set()
omoteF = False
uraF = False
for n in range(N - 1):
    for m in range(n + 1, N):
        tmp = 1 << n
        tmp += (1 << m)
        if AB[n][0] == AB[m][0]:
            omoteF = True
            if (AB[n][1] == AB[m][1] and n not in memo) or AB[n][1] != AB[m][1]:
                Data.add(tmp)
            if AB[n][1] == AB[m][1]:
                memo.add(n)
                memo.add(m)
        if AB[n][1] == AB[m][1]:
            if (AB[n][0] == AB[m][0] and n not in memo) or AB[n][0] != AB[m][0]:
                Data.add(tmp)
            uraF = True
            Data.add(tmp)
if omoteF:
    memo = set()
    for n in range(N - 1):
        for m in range(n + 1, N):
            tmp = 1 << n
            tmp += (1 << m)
            if AB[n][0] == AB[m][0]:
                omoteF = True
                if n not in memo:
                    Data.add(tmp)
                memo.add(n)
                memo.add(m)
if uraF:
    memo = set()
    for n in range(N - 1):
        for m in range(n + 1, N):
            tmp = 1 << n
            tmp += (1 << m)
            if AB[n][1] == AB[m][1]:
                uraF = True
                if n not in memo:
                    Data.add(tmp)
                memo.add(n)
                memo.add(m)
cards = 0
score = minMax(cards, True, -MAX, MAX)
print("Takahashi" if score > 0 else "Aoki")
