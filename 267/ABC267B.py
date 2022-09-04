Pin = [[7], [4], [8,2],[5,1],[9,3],[6],[10]]
PinIdx = {7: 0, 4: 1, 8: 2, 2: 2, 5: 3,1: 3,9: 4,3: 4,6: 5,10: 6}
S = input()
OneF = False
for n in range(10):
    if S[n] == '0':
        if n == 0:
            OneF = True
        Pin[PinIdx[n + 1]] .remove(n + 1)

PinFF = False
PinSF = False
PinSrF = False
for p in Pin:
    # 最初に立っている列
    if len(p) and not PinFF:
        PinFF = True
    # 立っている列があって次に倒れてる列が存在
    elif not len(p) and PinFF:
        PinSF = True
    # 立っている列があって次に倒れている列があって立っている列がある
    elif len(p) and PinFF and PinSF:
        PinSrF = True
if OneF and PinFF and PinSF and PinSrF:
    print('Yes')
else:
    print('No')
