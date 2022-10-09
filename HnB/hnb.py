import random


def hnb(I, O):
    fi = [True, True, True, True]
    fo = [True, True, True, True]
    h = 0
    b = 0
    for i in range(4):
        for o in range(4):
            if I[i] == O[o]:
                if not fi[i] or not fo[o]:
                    continue
                if i == o:
                    h += 1
                else:
                    b += 1
                fi[i] = False
                fo[o] = False
    return h, b


def calc(l, i, h, b):
    for idx in range(10000):
        if not l[idx]:
            continue
        o = ('0000' + str(idx))[-4:]
        h_, b_ = hnb(i, o)
        if h != h_ or b != b_:
            l[idx] = False
        if i == o:
            l[idx] = False
    for idx in range(10000):
        o = ('0000' + str(idx))[-4:]
        if i == o:
            print(idx, l[idx])


A = ('0000' + str(random.randint(0, 9999)))[-4:]
print(A)
L = [True for i in range(10000)]
for i in range(5):
    cnt = L.count(True)
    print(f'残り{cnt}個')
    I = ('0000' + input())[-4:]
    h, b = hnb(I, A)
    print(f"{h}Hit {b}Blow")
    calc(L, I, h, b)
