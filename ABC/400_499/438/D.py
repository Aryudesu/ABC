from atcoder.segtree import SegTree

def op(a, b):
    return max(a, b)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
SB = []
SC = []
sb = 0
sc = 0
for i in range(N):
    sb += B[i]
    sc += C[-i-1]
    SB.append(sb)
    SC.append(sc)
SC.reverse()
data = [0] * (N + 1)
for i in range(1, N):
    data[i] = SB[i - 1] + SC[i]
data[0] = SC[0]
data[-1] = SB[-1]

result = 0
st = SegTree(op, 0, data)
sa = 0
# print(data)
for i in range(N - 2):
    sa += A[i]
    maxData = st.prod(i+2, N)
    tmp = (maxData - SB[i]) + sa
    # print(sa, maxData, tmp)
    result = max(result, tmp)
print(result)
