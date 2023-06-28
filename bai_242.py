#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Kiểm tra độ dài của hai chuỗi
        if len(s) != len(t):
            return False
        
        # Khởi tạo bản đồ đếm cho các ký tự trong chuỗi `s`
        count_map = {}
        for char in s:
            if char in count_map:
                count_map[char] += 1
            else:
                count_map[char] = 1
        
        # Kiểm tra số lượng xuất hiện của các ký tự trong chuỗi `t`
        for char in t:
            if char in count_map:
                count_map[char] -= 1
                if count_map[char] < 0:
                    return False
            else:
                return False
        
        return True

# @lc code=end

