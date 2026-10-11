class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        a = 0
        n = len(nums)
        for i in range (0 ,len(nums)) :
            if n % (i+1) == 0:
                a += nums[i]**2
        return a        
        