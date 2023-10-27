class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        listFinal = list1 = list2 = []
        
        list1 = set(nums1)
        list2 = set(nums2)

        list11 = list1 - list2
        list22 = list2 - list1
        
        listFinal.append(list11)
        listFinal.append(list22)    

        return listFinal
