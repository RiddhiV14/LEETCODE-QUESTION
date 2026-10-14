
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        self.rev(nums, 0, n - 1)
        self.rev(nums, 0, k - 1)
        self.rev(nums, k, n - 1)

    def rev(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


        