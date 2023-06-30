#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # tạo mảng rỗng 
        res = []
        #Tạo một SortedList từ mảng con ban đầu có k phần tử từ mảng nums.
        w = SortedList(nums[:k])
        #Thêm vào danh sách kết quả số nguyên âm nhỏ thứ x của mảng con ban đầu. Nếu số này lớn hơn 0, thêm 0 vào danh sách kết quả.
        res.append(0 if w[x - 1] > 0 else w[x - 1])
        
        for i in range(k, len(nums)) :
            w.remove(nums[i - k])
            w.add(nums[i])
            res.append(0 if w[x - 1] > 0 else w[x - 1])
        return res
# @lc code=end

