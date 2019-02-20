n,m,a=map(int,input().split())

if(m%a==0):
  i=m//a
else:
  i=(m//a)+1
  
if(n%a==0):
  j=n//a
else:
  j=(n//a)+1
  
print(i*j)