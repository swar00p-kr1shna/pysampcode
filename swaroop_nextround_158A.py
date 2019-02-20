n,k=map(int, input().split())
m=list(map(int, input().split()))
count=0
for i in range(n):
    if(m[i]>k):
        count+=1
print(count)