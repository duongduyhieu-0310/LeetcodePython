#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        appear = [False] * n
        for num in nums:
            appear[num-1] = True
        for i in range(n):
            if not appear[i]:
                result.append(i+1)
        return result
# @lc code=end

