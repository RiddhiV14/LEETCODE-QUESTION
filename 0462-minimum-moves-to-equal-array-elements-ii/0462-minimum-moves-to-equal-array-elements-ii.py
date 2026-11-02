class Solution:
    def minMoves2(self, nums: list[int]) -> int:
       nums.sort()
       m = nums[len(nums)//2]
       a =0 
       for i in nums :
        if i> m :
            a += i - m
        else :
            a += m - i 
              
       return a       
        