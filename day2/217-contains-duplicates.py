def containDuplicates(nums):
    if len(set(nums))==len(nums):
        return False
    return True
nums=[1,2,3,1]
print(containDuplicates(nums))