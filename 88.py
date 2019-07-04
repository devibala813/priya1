p1,p2=map(int,input().split())
x1=p1
x2=p2
while(p2):
   p1,p2=p2,p1%p2
y1=(x1*x2)//p1
print(y1)
