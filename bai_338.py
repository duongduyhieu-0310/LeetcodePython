#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            s=str(bin(i))
            l.append(s.count('1'))
        return l
# @lc code=end

