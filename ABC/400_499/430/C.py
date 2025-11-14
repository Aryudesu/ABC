from bisect import bisect_left, bisect_right

N, A, B = map(int, input().split())
S = input()
a_data = []
b_data = []
a_count = 0
b_count = 0
for i in range(N):
    b_data.append(b_count)
    if S[i] == "a":
        a_count += 1
    if S[i] == "b":
        b_count += 1
    a_data.append(a_count)
# print(a_data)
# print(b_data)
result = 0
for i in range(N):
    a = a_data[-i-1]
    b = b_data[-i-1]
    # Aギリギリまで詰めれる場所
    idx1 = bisect_right(a_data, max(a - A - 1, 0))
    # Bギリギリまで取れる場所
    idx2 = bisect_left(b_data, max(b - B, 0))
    # print("debug", idx1, idx2)
    if idx1 >= N:
        continue
    if idx1 >= idx2 and a_data[-i-1] - a_data[idx1] >= A:
        result += idx1 - idx2
print(result)
