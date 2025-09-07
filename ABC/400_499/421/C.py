N = int(input())
S = input()
# Bを偶数インデックスに移動させるための操作回数
e = 0
eres = 0
# Bを奇数インデックスに移動させるための操作回数
o = 0
ores = 0
bc = 0
for i in range(2 * N):
    if S[i] == "B":
        e_target = bc * 2
        eres += abs(e_target - i)
        o_target = bc * 2 + 1
        ores += abs(o_target - i)
        bc += 1
print(min(ores, eres))
