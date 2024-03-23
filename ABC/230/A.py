N = int(input())
if N >= 42:
    num = str(N + 1).zfill(3)
else:
    num = str(N).zfill(3)
print("AGC" + num)
