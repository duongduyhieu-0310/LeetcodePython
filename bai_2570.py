#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#

# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        b = []
        for i in nums1:
            for j in nums2:
                if i[0] == j[0]:
                    c = [i[0], i[1] + j[1]]
                    b.append(c)
                    nums2.remove(j) # Loại bỏ cặp số đã được ghép từ nums2
                    break
            else:
                b.append(i)
        
        # Thêm các cặp số còn lại trong nums2 vào danh sách kết quả
        for k in nums2:
            b.append(k)
        b.sort()
        return b

# @lc code=end

