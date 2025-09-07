from collections import deque

def calcCollisionNum(Rt: int, Ct: int, Ra: int, Ca: int, Td: int, Ad: int, Tn: int, An: int) -> int:
    """
    (Rt, Ct)と(Ra, Ca)からTd, AdにTn, An移動したときの交差判定をしたい
    Td, Adは0が下，1が右とする．
    """
    # 元々同じ位置の場合
    if Rt == Ra and Ct == Ca:
        # 同じ方向に移動した場合
        if Td == Ad and Tn == An:
            return abs(Tn)
        return 0
    # 高橋を原点に移動
    Rt, Ra = 0, Ra - Rt
    Ct, Ca = 0, Ca - Ct
    # 青木を右に移動
    if Ca < 0:
        Ca = -Ca
        # 移動方向変更
        if Ad == 1:
            An = -An
        if Td == 1:
            Tn = -Tn
    # 青木を下に移動
    if Ra < 0:
        Ra = -Ra
        if Ad == 0:
            An = -An
        if Td == 0:
            Tn = -Tn
    # 青木が下か右に移動，もしくは高橋が上か左に移動したらNG
    if An > 0 or Tn < 0:
        return 0
    # お互い上下移動
    if Ad == 0 and Td == 0:
        return 1 if Ca == 0 and Ra <= abs(Tn) * 2 and Ra % 2 == 0 else 0
    # お互い左右移動
    if Td == 1 and Ad == 1:
        return 1 if Ra == 0 and Ca <= abs(Tn) * 2 and Ca % 2 == 0 else 0
    # お互い直行移動
    if Td != Ad:
        return 1 if Ra == Ca and Ra <= abs(Tn) else 0
    return 0





Rt, Ct, Ra, Ca = [int(l) for l in input().split()]
N, M, L = [int(l) for l in input().split()]
SA = deque()
TB = deque()
for m in range(M):
    s, a = input().split()
    SA.append([s, int(a)])
for l in range(L):
    t, b = input().split()
    TB.append([t, int(b)])
result = 0
while len(SA):
    sa = SA.popleft()
    tb = TB.popleft()
    pRt, pCt, pRa, pCa = Rt, Ct, Ra, Ca
    num = min(sa[1], tb[1])
    Td = None
    Ad = None
    Tn = num
    An = num
    if sa[1] == tb[1]:
        pass
    elif sa[1] > tb[1]:
        sa[1] -= num
        SA.appendleft(sa)
    else:
        tb[1] -= num
        TB.appendleft(tb)
    if sa[0] == "R":
        Td = 1
        Tn = num
        Ct += num
    elif sa[0] == "L":
        Td = 1
        Tn = -num
        Ct -= num
    elif sa[0] == "U":
        Td = 0
        Tn = -num
        Rt -= num
    elif sa[0] == "D":
        Td = 0
        Tn = num
        Rt += num
    if tb[0] == "R":
        Ad = 1
        An = num
        Ca += num
    elif tb[0] == "L":
        Ad = 1
        An = -num
        Ca -= num
    elif tb[0] == "U":
        Ad = 0
        An = -num
        Ra -= num
    elif tb[0] == "D":
        Ad = 0
        An = num
        Ra += num
    result += calcCollisionNum(pRt, pCt, pRa, pCa, Td, Ad, Tn, An)
print(result)
