#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a=[]
        b=set()
        for i in nums:
            if i in b:
                a.append(i)
            else:
                b.add(i)
        
        # Tạo một danh sách mới chỉ chứa các phần tử không chung của hai danh sách ban đầu
        x1_new = [item for item in nums if item not in a]
        return sum(x1_new)
# @lc code=end

