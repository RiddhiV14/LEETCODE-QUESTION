class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suffix = [0]*len(nums)
        prefix = [0]*len(nums)
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range (len(nums) -2 , -1 , -1):
            suffix[i]= min(nums[i],suffix[i +1])
        prefixmax= nums[0]    
        for j in range(len(nums)):
            prefixmax= max(prefixmax,nums[j])
            if prefixmax -suffix[j] <= k :
                return j
        return -1        