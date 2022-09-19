class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        num1Copy = nums1[:m]
        p1,p2 = 0,0
        
        for p in range(m+n):
            if p2 >= n or (p1 < m and num1Copy[p1] <= nums2[p2]):
                nums1[p] = num1Copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
                
                
        return nums1
        