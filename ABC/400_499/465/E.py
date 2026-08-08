def calc(num: str)->int:
    MOD = 998244353
    dp = []
    L = len(num)
    # 桁
    for _ in range(L):
        tmp0 = []
        # 大小
        for _ in range(2):
            tmp1 = []
            # 数字フラグ
            for _ in range(1 << 10):
                tmp1.append(0)
            tmp0.append(tmp1)
        dp.append(tmp0)
    m = int(num[0])
    print(dp)


N = input()
result = calc(N)
