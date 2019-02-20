n=int(input())
val1=val2=val3=0
for i in range(n):
    command=input()
    if(command=="X++" or command=="++X"):
        val1+=1
    elif(command=="X--" or command=="--X"):
        val2+=-1
    else:
        val3+=0
    
print(val1+val2+val3)