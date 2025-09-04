class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            k = k % len(nums)
            j = 0
            temp = [0]*k
            for i in range(k,0,-1):
                index = len(nums)-i
                #print(index)
                temp[j] = nums[index]
                j+=1
            #print(temp)
            j=0
            for i in range(len(nums)-k-1, -1, -1):
                index = len(nums)-j-1
                #print(index)
                nums[index] = nums[index-k]
                j+=1
            #print(nums)
            for i in range(0,k):
                nums[i] = temp[i]
            #print(nums)

    
