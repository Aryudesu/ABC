base = 37
MOD = 10**9 + 9
base_rev = pow(base, MOD-2, MOD)

result = []
T = int(input())
for t in range(T):
    A = input()
    B = input()
    a_hash = 0
    # a_0 * b**(|A|-1) + a_1 * b**(|A|-2) + ...
    for a in A:
        a_hash = (a_hash * base + int(a)) % MOD
    b_hash = 0
    for b in B:
        b_hash = (b_hash * base + int(b)) % MOD
    if a_hash == b_hash:
        result.append(0)
        continue
    # 一部分ロリハ（引く用）
    a_tip1 = a_hash
    # 引くやつにかける冪
    r_pow = pow(base, len(A)-1, MOD)
    count = 0
    f = False
    for a in A:
        count += 1
        a_tip1 = ((a_tip1 - r_pow * int(a)) * base) % MOD
        a_tip1 += int(a)
        if a_tip1 == b_hash:
            f = True
            break
    if f:
        result.append(count)
    else:
        result.append(-1)
for r in result:
    print(r)

