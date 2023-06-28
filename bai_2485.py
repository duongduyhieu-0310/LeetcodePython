#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
  def pivotInteger(self, n: int) -> int:
    a = [i for i in range(1, n+1)]
    for i in range(len(a)):
        sum1 = sum(a[:i])
        sum2 = sum(a[i+1:])
        if sum1 == sum2:
            return a[i]
    return -1
# @lc code=end

