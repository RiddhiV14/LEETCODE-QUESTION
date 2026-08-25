class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = 1
        s = set(nums)
        while  True:
            if k*n in s :
                n += 1
            else :
                return k*n



        