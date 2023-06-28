#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        res, n = 0, 0
        for i in nums:
            if i!=0: n+=1
            else:
                res = max(n,res)
                n=0
        return res
# @lc code=end

