class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newI = 0
        for x in nums:
            if x != 0:
                nums[newI] = x
                newI = newI + 1
        for i in range(newI, len(nums)):
            nums[i] = 0
