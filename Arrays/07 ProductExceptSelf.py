class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            mult = mult * nums[i]
        multSkip = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = int(mult / nums[i])
                multSkip = multSkip * nums[i]
            else:
                for j in range(i+1, len(nums)):
                    multSkip = multSkip * nums[j]
                res[i] = int(multSkip)
        return res    
