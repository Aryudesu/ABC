MOD = 10 ** 9 + 7
N = int(input())
S = input()
data = [0] * 7
st = {"atcoder"[i]: i for i in range(7)}
# print(st)
for s in S:
    ds = st.get(s)
    if ds is None:
        continue
    if ds == 0:
        data[ds] = (data[ds] + 1) % MOD
    elif ds <= 6:
        data[ds] = (data[ds] + data[ds - 1]) % MOD
print(data[-1])
