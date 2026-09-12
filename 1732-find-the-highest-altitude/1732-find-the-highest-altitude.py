class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = 0
        b = 0
        for i in range (0 , len(gain)) :
            a = gain[i] + a
            b = max(a , b)  
        return b    

      
        