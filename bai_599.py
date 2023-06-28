#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Tạo một dictionary để lưu trữ tổng chỉ số của từng chuỗi trong list1
        index_dict = {}
        for i, s in enumerate(list1):
            index_dict[s] = i
        
        # Duyệt qua từng cặp chuỗi trong list2 và tính tổng chỉ số của từng cặp chuỗi
        min_sum = float('inf')
        res = []
        for i, s in enumerate(list2):
            if s in index_dict:
                curr_sum = i + index_dict[s]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    res = [s]
                elif curr_sum == min_sum:
                    res.append(s)
                    
        return res

# @lc code=end

