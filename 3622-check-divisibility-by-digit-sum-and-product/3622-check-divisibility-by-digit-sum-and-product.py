class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum =0
        pro = 1
        n1 = n
        while n1>0:
            sum = sum+ (n1%10)
            pro = pro*(n1%10)
            n1 = n1//10
        if (n%(sum + pro)==0):
            return True
        else :
            return False       

        