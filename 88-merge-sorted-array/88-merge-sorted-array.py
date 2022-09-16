class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[m:] = nums2
        
        for i in range(len(nums1)):
            j = i + 1
            while j < len(nums1):
                if nums1[i] > nums1[j]:
                    nums1[i],nums1[j] = nums1[j],nums1[i]
                j += 1
        
        