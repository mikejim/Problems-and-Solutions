class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = 0
        b = 0
        suma = 0
        maxCeros = 0
        while b < len(nums):
            suma = suma + nums[b]
            if (b - a + 1) - suma > k:
                suma = suma - nums[a]
                a = a + 1
            else:
                if (b - a + 1) > maxCeros:
                    maxCeros = (b - a + 1)
            b = b + 1
        return maxCeros     
    