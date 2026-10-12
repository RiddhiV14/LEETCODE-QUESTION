
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            left = i + 1
            right = n - i
            count = (left * right + 1) // 2
            total += arr[i] * count

        return total

        