#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        s = []
        for i in range(1,n//2+1):
            s.append(i)
            s.append(-i)
        if n % 2 != 0:
            s.append(0)
        return s
# @lc code=end

