#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [str(x) for x in nums]
    
        ans = 0
        for num in nums:
            if len(num) % 2 == 0:
                ans += 1
                
        return ans
# @lc code=end

