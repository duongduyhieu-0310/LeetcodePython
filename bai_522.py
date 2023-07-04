#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#

# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # tạo set rỗng
        s = set(nums)
        #nếu k=0 trả về số lg phần tử  mà có count xuất hiện 
        if k == 0: return sum(1 for x in s if nums.count(x) > 1)
         # th còn lại
        return sum(1 for x in s if x + k in s)
# @lc code=end

