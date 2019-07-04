p1,p2=map(int,input().split())
maxima=max(p1,p2)
while(1):
   if(maxima%p1==0 and maxima%p2==0):
         print(maxima)
         break
   maxima+=1
