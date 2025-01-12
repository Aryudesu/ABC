from itertools import permutations

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("(1)")
for i in permutations(nums, 6):
    if i[0] == 0 or i[2] == 0 or i[5] == 0:
        continue
    if int(f"{i[0]}{i[1]}") * int(f"{i[2]}{i[3]}{i[4]}{i[5]}") == int(f"{i[5]}{i[4]}{i[3]}") * int(f"{i[2]}{i[1]}{i[0]}"):
        print(i)
print("(2)")
for i in permutations(nums, 8):
    if i[0] == 0 or i[3] == 0 or i[7] == 0:
        continue
    if int(f"{i[0]}{i[1]}{i[2]}") * int(f"{i[3]}{i[4]}{i[5]}{i[6]}{i[7]}") == int(f"{i[7]}{i[6]}{i[5]}{i[4]}") * int(f"{i[3]}{i[2]}{i[1]}{i[0]}"):
        print(i)
print("(3)")
for i in permutations(nums, 10):
    if i[0] == 0 or i[4] == 0 or i[9] == 0:
        continue
    if int(f"{i[0]}{i[1]}{i[2]}{i[3]}") * int(f"{i[4]}{i[5]}{i[6]}{i[7]}{i[8]}{i[9]}") == int(f"{i[9]}{i[8]}{i[7]}{i[6]}{i[5]}") * int(f"{i[4]}{i[3]}{i[2]}{i[1]}{i[0]}"):
        print(i)
