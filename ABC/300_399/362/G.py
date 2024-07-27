import bisect

from atcoder.string import suffix_array

S = input()
s_arr = suffix_array(S)
Q = int(input())
result = []
for _ in range(Q):
    T = input()
    l = bisect.bisect_left(s_arr, T, key=lambda x: S[x: x + len(T)])
    r = bisect.bisect(s_arr, T, key=lambda x: S[x: x + len(T)])
    result.append(r - l)
for r in result:
    print(r)
