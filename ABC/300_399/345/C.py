S = input()
data = dict()
for s in S:
    data[s] = data.get(s, 0) + 1
alp = "abcdefghijklmnopqrstuvwxyz"
result = 0
oneF = False
for a in range(len(alp)):
    for b in range(a + 1, len(alp)):
        result += data.get(alp[a], 0) * data.get(alp[b], 0)
    # 2つ以上同じ文字がある場合は元文字列を含む
    if data.get(alp[a], 0) > 1:
        oneF = True
# 元の文字列を考慮しないといけない場合
if oneF:
    result += 1
print(result)
