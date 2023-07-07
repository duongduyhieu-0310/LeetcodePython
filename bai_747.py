#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        i= nums.index(m)
        nums.remove(m)
        nums.insert(i,0)
        m1= max(nums)
        i1=nums.index(m1)
        if m>=m1*2:
            return i
        else:
            return -1
# @lc code=end

