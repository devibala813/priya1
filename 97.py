s1=int(input())
s2=0
while(s>0):
   s3=s1%10
   s2=s2*10+s3
   s1=s1//10
print(s2)
