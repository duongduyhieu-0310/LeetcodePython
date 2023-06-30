#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            # xoá phần tử cuối mảng
            last=nums.pop()
            # thêm số vừa xoá vào đầu mảng 
            nums.insert(0,last)
        
        
# @lc code=end

