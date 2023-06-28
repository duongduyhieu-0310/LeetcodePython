#
# @lc app=leetcode id=2455 lang=python3
#
# [2455] Average Value of Even Numbers That Are Divisible by Three
#

# @lc code=start
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        count = 0

        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                s += i
                count += 1
                
        if count > 0:
            return s / count
        else:
            return 0

# @lc code=end

