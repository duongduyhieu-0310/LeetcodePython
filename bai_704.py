#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r - l >= 0:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return - 1

# @lc code=end

