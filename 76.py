s2=int(input())
if(s2>1):
   for i in range (2,s2):
      if(s2%i==0):
       print("yes")
       break
   else:
      print("no")
