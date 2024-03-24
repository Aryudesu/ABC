# もうマヂムリ・・・・・・

def calc():
    N = int(input())
    A_ = [int(l) for l in input().split()]
    B_ = [int(l) for l in input().split()]
    # 2つが同じ場合
    if A_ == B_:
        return 'Yes'
    B = []
    pc = -1
    for b in B_:
        if pc != b:
            B.append(b)
            pc = b
    A = []
    pc = -1
    for a in A_:
        if a not in B:
            continue
        if pc != a:
            A.append(a)
            pc = a
    lA = len(A)
    lB = len(B)
    # Bに一致する要素がAに全く存在しない場合
    # Aが一周して2つ要素が必要になった場合 A = 2 3 1 3, B = 2 1 2 1の場合
    if lA == 0 or lA + 1 < lB:
        return 'No'
    # Aから削れる要素がないのに移動せざるを得ない場合
    if N == lB:
        return 'No'
    for ai in range(lA):
        res = True
        for bi in range(lB):
            if A[(ai + bi) % lA] != B[bi]:
                res = False
                break
        if res:
            return 'Yes'
    return 'No'


result = []
T = int(input())
for t in range(T):
    result.append(calc())
for r in result:
    print(r)
