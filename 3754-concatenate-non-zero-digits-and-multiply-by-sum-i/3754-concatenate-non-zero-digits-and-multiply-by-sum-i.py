class Solution:
    def sumAndMultiply(self, n: int) -> int:
        no = 0
        p =1
        sum = 0
        while n>0 :
            if n%10!= 0:
                no= no + (n%10)*p
                sum = sum + n%10
                p = p *10
            n = n//10
        return no*sum        
               
        