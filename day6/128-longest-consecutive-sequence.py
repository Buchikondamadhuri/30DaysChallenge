nums=[100,4,200,1,3,2]
sorted_set=list(sorted(set(nums)))
print(sorted_set)
ans=0
for i in range(len(sorted_set)-1):
    if sorted_set[i]+1==sorted_set[i+1]:
       ans+=1
if sorted_set[-1]-1==sorted_set[-2]:
    ans+=1
print(ans)

