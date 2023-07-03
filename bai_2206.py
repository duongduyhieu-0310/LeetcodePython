#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a = []
        l = len(nums)
        for i in range(0, l, 2):
            # Thêm cặp giá trị trong mảng `nums` vào danh sách `a`
            # Sử dụng index để truy cập vào cặp giá trị
            a.append([nums[i], nums[i + 1]])
        
        b = set()
        for j in a:
            if j[0] == j[1]:
                b.add(0)
            else:
                b.add(1)
        
        if b == {0}:
            return True
        else: 
            return False

# @lc code=end

