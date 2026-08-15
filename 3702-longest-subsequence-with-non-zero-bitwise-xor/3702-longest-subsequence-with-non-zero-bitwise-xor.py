class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        for i in nums : 
            xor = xor ^ i 
        if xor != 0:
            return len(nums)
        else :
            return len(nums)- 1 if any(i != 0 for i in nums) else 0       
            

        