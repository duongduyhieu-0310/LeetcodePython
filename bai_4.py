class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # gộp hai mảng và sắp xếp 
        nums= nums1+nums2
        n=len(nums)
        nums.sort()
        # tính medium 
        if n%2==0:
            medium=(nums[n//2]+nums[n//2-1])/2.0
        else:
            medium=nums[n//2]
        return medium 
         

      