class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            if curr + nums[i] > nums[i]:
                curr = curr + nums[i]
            else:
                curr = nums[i]

            if curr > best:
                best = curr

        return best
        