class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        longest = 0
        s = set(nums)
        for i in s :
            if i-1 not in s:
                current = i
                count = 1
                while current+1 in s:
                     count += 1
                     current += 1
                longest = max (count, longest)    
        return longest        

        return count     

        