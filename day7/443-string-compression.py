chars = ["a","a","b","b","c","c","c"]
dici={}
for i in chars:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
ans=[]
for i,j in dici.items():
    if j!=1:
        ans.append(i)
        ans.append(j)
    if j>9:
        for i in range(len(str(j))):
            ans.append(j%10)
            j=j//10
if len(ans)>1:
    print(ans)
    print(len(ans))
else:
    print("1")
