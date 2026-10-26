class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
       a = [[]]
       for num in nums :
        for i in range(len(a)):
            s = a[i] + [num]
            a.append(s)
       return a     
      
        