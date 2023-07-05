#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year,month,day=map(int,date.split("-"))
        if (year%400==0 or (year%100!=0 and year%4==0))and month>2:
            day+=1
        for i in range(1,month):
            day+=month_days[i-1]
        return day
# @lc code=end

