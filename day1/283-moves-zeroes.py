nums = [0,1,0,3,12]
z_index = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[z_index], nums[i] = nums[i], nums[z_index]
        z_index += 1
print(nums)