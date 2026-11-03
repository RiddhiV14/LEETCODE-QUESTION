class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        a = 0
        for i in nums :
            a += m- i 
        return a     
        