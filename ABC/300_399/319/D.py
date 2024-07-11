N, M = [int(l) for l in input().split()]
L = [int(l) for l in input().split()]
su = 0
for l in L:
    su += l + 1
su -= 1


# 指定幅で収めることができるか
def check(num):
    ln = 1
    wn = 0
    for l in L:
        # 単語が幅に入らなければ駄目
        if l > num:
            return False
        # 幅に収まらなければ改行
        if wn + l > num:
            ln += 1
            wn = l + 1
            wf = True
        else:
            # ぴったりの場合1マス開ける必要がある
            if wn + l >= num:
                wn = 0
                ln += 1
                wf = False
            else:
                wn += l + 1
                wf = True
        if ln > M and wf:
            return False
    return True


l = 1
r = su
while True:
    if l + 1 == r:
        break
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid
if check(l):
    print(l)
else:
    print(r)
