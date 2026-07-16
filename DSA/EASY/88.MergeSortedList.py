class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:]=nums1[:m]
        nums1.extend(nums2)
        nums1.sort()
   
        return nums1
