#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        for i in arr:
            a=arr.count(i)
            if i==a:
                return i
        else: 
                return -1

        
# @lc code=end

