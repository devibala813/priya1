n1,n2=input().split()
n1=int(n1)
n2=int(n2)
m=list(map(int,input().split()))
m.sort()
print(m[n2-1])
