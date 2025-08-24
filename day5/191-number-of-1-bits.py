n = 11
bits=""
ans=0
while n>0:
    temp=str(n%2)
    bits+=temp  
    n//=2
    if temp=="1":
       ans+=1
print(ans)