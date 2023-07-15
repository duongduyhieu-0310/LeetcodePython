#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
import numpy as np
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        arr=np.array(nums)
        # tìm tổng các phần tử khi ta làm gọn mảng 
        c=np.sum(np.unique(arr))
        # tổng các phần tử trong mảng 
        b=np.sum(arr)
        return c*2-b
# @lc code=end

