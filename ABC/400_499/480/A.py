# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary
S1 = input()
S2 = input()
key1 = {S1[0], S2[0]}
key2 = {S1[0], S1[1]}
key3 = {S1[1], S2[1]}
key4 = {S2[0], S2[1]}
if "A" in key1 and "D" in key1:
    print("Yes")
elif "A" in key2 and "D" in key2:
    print("Yes")
elif "A" in key3 and "D" in key3:
    print("Yes")
elif "A" in key4 and "D" in key4:
    print("Yes")
else:
    print("No")
