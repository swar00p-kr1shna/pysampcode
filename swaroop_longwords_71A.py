n=int(input())
for i in range(n):
 name=input()
 if len(name)>10:
    s=name[1:-1]
    print(name[0]+""+str(len(s))+""+name[-1])
 else:
    print(name)