class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = {}
        for i in range (0, len(nums)) :
            s =  target - nums[i]
            if s in f :
                return [f[s],i]
            f[nums[i]]= i     