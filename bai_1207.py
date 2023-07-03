#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Tạo từ điển để đếm số lần xuất hiện của mỗi giá trị
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        # Kiểm tra xem số lần xuất hiện có duy nhất hay không
        occurrence_set = set(counts.values())
        return len(occurrence_set) == len(counts)
# @lc code=end

