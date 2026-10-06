class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = []
        a = 0
        for i in s :
            if i == "(":
                c.append(1)
            else : 
                if len(c)> 0 :
                    c.pop()
                else :
                    a += 1
        return len(c) + a 