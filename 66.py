dr=int(input())
if(dr>1):
   for i in range(2,dr):
      if(dr%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
