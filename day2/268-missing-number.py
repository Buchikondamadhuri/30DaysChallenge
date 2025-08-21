def missingNumber(nums):
    n=len(nums)
    sum1=int(n*(n+1)/2)
    sum2=0
    for i in range(len(nums)):
        sum2+=nums[i]
    return sum1-sum2  
nums=[3,0,1]
print(missingNumber(nums))
