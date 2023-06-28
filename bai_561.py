#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sắp xếp mảng từ nhỏ đến lớn
        nums.sort()
        
        # Tính tổng các cặp số nhỏ nhất
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        
        return sum


# @lc code=end

