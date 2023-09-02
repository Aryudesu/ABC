S=""
for _ in range(10):S+=input()
t,s=S.find("#"),S.rfind("#")
print(t//10+1, s//10+1, t%10+1, s%10+1)