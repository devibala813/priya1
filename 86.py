ch1=list(input())
ch2=[]
for i in ch1:
   if(i not in ch2):
      ch2.append(i)
if(ch1=ch2):
   print("Yes")
else:
   print("No")
   
