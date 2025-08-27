nums=[2,0,2,1,1,0]
l=0
mid=0
r=len(nums)-1
while mid<=r:
    if nums[mid]==0:
        nums[mid],nums[l]=nums[l],nums[mid]
        l+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    elif nums[mid]==2:
        nums[mid],nums[r]=nums[r],nums[mid]
        r-=1
print(nums)
            