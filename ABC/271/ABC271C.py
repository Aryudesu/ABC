# https://atcoder.jp/contests/abc271/editorial/4937

N = int(input())
A = {int(l) for l in input().split()}
l = 0
r = N + 1
while r - l > 1:
    m = (r + l)//2
    # m巻までに持ってるやつ
    c = len(set(range(1, m+1)) & A)
    if (c + (N - c)//2) >= m:
        l = m
    else:
        r = m
print(l)
