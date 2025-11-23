from atcoder.fenwicktree import FenwickTree
MaxNum = 500000
N, Q = map(int, input().split())
A = list(map(int, input().split()))
# 値管理
data1 = FenwickTree(MaxNum + 5)
# 個数管理
data2 = FenwickTree(MaxNum + 5)
for a in A:
    data1.add(a, a)
    data2.add(a, 1)
result = []
for q in range(Q):
    num, *query = map(int, input().split())
    if num == 1:
        x, y = query
        a = A[x-1]
        data1.add(a, -a)
        data1.add(y, y)
        data2.add(a, -1)
        data2.add(y, 1)
        A[x-1] = y
    elif num == 2:
        l, r = query
        if l > r:
            result.append(l * N)
        else:
            l_num = data2.sum(0, l)
            r_num = data2.sum(r, MaxNum+3)
            m_sum = data1.sum(l, r)
            result.append(l*l_num + r * r_num + m_sum)
    else:
        raise Exception()
for r in result:
    print(r)
