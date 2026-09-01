class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range (0 , len(nums)):
            left = 0
            right = len(nums)-1
            sum1 = sum(nums[ : i])
            sum2 = sum(nums[i+1:])
            if sum1 == sum2 :    
                 return i    
        return -1            


