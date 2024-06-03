def find_sum(index,n,nums):
    if index == n:
        return 0   
    next_ele = find_sum(index+1,n,nums) 
    return next_ele + nums[index] 
nums = [1,2,3,4,5] 
n = len(nums) 
print(find_sum(0,n,nums)) 
