nums1=[4,9,5]
nums2=[9,4,9,8,4]
dici={}
ans=[]
for i in range(len(nums1)):
    if nums1[i] not in dici:
        dici[nums1[i]]=1
    else:
        dici[nums1[i]]+=1
for i in nums2:
    if i in dici and dici[i]>0:
        ans.append(i)
        dici[i]-=1
print(ans)

