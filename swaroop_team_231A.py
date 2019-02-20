n=int(input())
count=0
for i in range(n):
    n,m,k=map(int,input().split())
    if((n==1 and m==0 and k==0) or (n==0 and m==1 and k==0) or (n==0 and m==0 and k==1) or (n==0 and m==0 and k==0)):
       count+=0
    else:
        count+=1
        
print(count)