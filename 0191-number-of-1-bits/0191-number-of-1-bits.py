class Solution:
    def hammingWeight(self, n: int) -> int:
        a = str(bin(n))
        c =0
        for i in a :
            if i == "1" :
                c = c+1
        return c        

        