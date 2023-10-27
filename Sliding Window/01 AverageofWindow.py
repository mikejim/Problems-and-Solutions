class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = 0
        if len(nums) == 1:
            return nums[0]
        suma = 0
        for i in range(len(nums)):
            suma = suma + nums[i]
            if i == k-1:
                average = suma/k
            else:
                if i >= k:
                    suma = suma - nums[i-k]
                    newA = suma/k
                    if newA > average:
                        average = newA
        return average
