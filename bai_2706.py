#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if prices[0]+prices[1]>money:
            return money
        return money-(prices[0]+prices[1])
# @lc code=end

