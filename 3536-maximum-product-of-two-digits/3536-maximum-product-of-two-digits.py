class Solution:
    def maxProduct(self, n: int) -> int:
        a =[]
        pro = 1
        pro1 =1
        count = 0
        while n> 0 :
            a.append(n%10)
            n = n//10
        a.sort( reverse = "Ture")
        return a[0]*a[1]               
          


        