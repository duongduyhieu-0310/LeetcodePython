#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if i>0:
                a.append(i)
            else:
                b.append(i)
        c=[]
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c


# @lc code=end

