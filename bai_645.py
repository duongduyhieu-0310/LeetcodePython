#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a , b = None, None
        l = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in l:
                a =i
            if l[i]>1:
                b =i
        return[b,a]
# @lc code=end

