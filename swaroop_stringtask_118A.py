m= input()
m = m.lower()
n = ""
P= ['a' , 'e' , 'i' , 'o' , 'u' , 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for i in range(0,len(m)):
    if m[i] not in P:
        n+='.'
        n+=m[i]
        
print(n)