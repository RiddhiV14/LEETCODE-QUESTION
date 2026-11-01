class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        a =0
     
        for i in nums :
            a += i - m
        return a    

        