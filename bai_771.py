#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_jewels =0
        for i in jewels:
            count_jewels += stones.count(i)

        return count_jewels
# @lc code=end

