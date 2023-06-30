#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sắp xếp lại mảng theo chiều giảm dần độ lớn
        a=sorted(nums,reverse=True)
        return a[k-1]
            
# @lc code=end

