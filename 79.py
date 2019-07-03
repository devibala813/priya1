r1,r2=map(int,input().split())
for i in range(0,(r1*r2)+1):
   if(r1**r2==0):
      print("yes")
      break
else:
   print("no")
