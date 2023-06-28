#
# @lc app=leetcode id=2605 lang=python3
#
# [2605] Form Smallest Number From Two Digit Arrays
#

# @lc code=start
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return int(i)
        
        
        x=str(min(nums1))
        y=str(min(nums2))
        z=int(x+y)
        q=int(y+x)
        c=min(z,q)
        return c
# @lc code=end

