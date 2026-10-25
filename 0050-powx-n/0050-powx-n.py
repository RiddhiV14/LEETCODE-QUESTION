
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        power = abs(n)

        while power > 0:
            if power % 2 == 1:
                result *= x
            x *= x
            power //= 2

        if n < 0:
            result = 1.0 / result

        return result

        