nums=[1]
'''dici={}
for i in range(len(nums)):
    if nums[i] not in dici:
        dici[nums[i]]=1
    else:
        dici[nums[i]]+=1
for i,j in dici.items():
    if j==1:
        print(i)'''
ans=0
for i in range(len(nums)):
    ans^=nums[i]
print(ans)
