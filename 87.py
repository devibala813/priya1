w1,w2=map(int,input().split())
n=1
while(n<=w1 and n<=w2):
   if(w1%n==0 and w2%n==0):
      gcd=n
   n=n+1
print(gcd)
