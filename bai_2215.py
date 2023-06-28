#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = set(nums1)
        y = set(nums2)
        z = x.intersection(y)
        x1, x2, x3 = list(x), list(y), list(z)

        # Xóa các phần tử chung với đoạn code x1 và x3
        new1=[item for item in x1 if item not in x3]
        
        # Xóa các phần tử chung với đoạn code x2 và x3
        
        new2=[item for item in x2 if item not in x3]
        return (new1,new2)
# @lc code=end

