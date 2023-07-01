#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a = 1
        high = n
        result = 0
        
        while a <= high:
            mid = (a+high)//2
            b = isBadVersion(mid)
            if b == True:
                result = mid
                high = mid - 1
            elif b == False:
                a = mid + 1
        return result
# @lc code=end

