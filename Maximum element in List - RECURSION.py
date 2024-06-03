def find_max(index,n,nums):
  if index == n-1:
    return nums[index] 
  maxi = find_max(index+1,n,nums) 
  return max(maxi,nums[index])  
nums = [1,2,3,4,5] 
n = len(nums) 
print(find_max(0,n,nums)) 
