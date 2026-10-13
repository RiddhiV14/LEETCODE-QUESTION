class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        a = 0
        max = 0
        for i in nums :
            if i == 1 :
                a += 1 
                if a> max :
                    max = a
            else :
                a = 0
        return max        
