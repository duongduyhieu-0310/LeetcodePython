#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        a=[0,1,1]
        for i in range(n-2):
            b=a[i]+a[i+1]+a[i+2]
            a.append(b)
        return a[n]
# @lc code=end

