#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
       # tạo tất cả hoán vị của nums
       perm = list(itertools.permutations(nums))
       #loại bỏ cấc phần tử trùng lặp 
       new_list = list(set(perm))
       # trả về kết qủa 
       return new_list
# @lc code=end

