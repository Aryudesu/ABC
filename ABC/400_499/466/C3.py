n = int(input())
ans = 0
p = 1
d = 1
while d < n:
  while p+d <= n:
    print("?",p,p+d,flush=True)
    txt = input()
    if txt == 'Yes':
      ans += 1
    p += 1
  p = 1
  d += 1
print('!',ans)
exit(0)
