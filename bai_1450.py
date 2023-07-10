#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len( endTime)):
            if startTime[i]<= queryTime <= endTime[i]:
                count=count+1
        return count

# @lc code=end

