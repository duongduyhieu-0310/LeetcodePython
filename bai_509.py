#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        a=(5**(0.5))
        s=(1/a)*( ((1+a)/2)**n - ((1-a)/2)**n )
        
        return int(s)

# @lc code=end

