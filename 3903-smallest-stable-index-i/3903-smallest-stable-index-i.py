class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range (0,len(nums)) :
            a = max(nums[:i+1])
            b = min(nums[i:])
            if a-b <= k :
                return i 
        return -1  


            