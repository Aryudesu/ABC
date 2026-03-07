from collections import defaultdict

INF = 10 ** 18
N, K, B = map(int, input().split())
CS = []
for n in range(N):
    c, s = map(int, input().split())
    CS.append((c, s))
# やりたいことは，各山に対して，予算と登頂した個数とどの山を登ったか？をキーに，前に登った山の高さを最小化？
dp = defaultdict(lambda:INF)
# (予算，個数) = 高さ
dp[(0, 0)] = 0
for nextIdx in range(N):
    c, s = CS[nextIdx]
    nextDP = dp.copy()
    for key in dp:
        nowTakasa = dp[key]
        if nowTakasa >= s:
            continue
        yosan, kosu = key
        nextKosu = kosu + 1
        if nextKosu > K:
            continue
        nextYosan = yosan + c
        if nextYosan > B:
            continue
        nextDP[(nextYosan, nextKosu)] = min(nextDP[(nextYosan, nextKosu)], s)
    dp = nextDP
    # print(dp)
result = 0
for yosan, kosu in dp:
    result = max(kosu, result)
print(result)
# ACしましたｄ
