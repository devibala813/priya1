dd1=str(input())
s=list(dd1)
r=len(dd1)
p=""
if r%2==0:
   s[int(r/2)]=="*"
   s[int(r/2-1)]=="*"
else:
   s[int(r/2)]=="*"
p=p.join(s)
print(p)
