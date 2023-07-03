#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 in nums:
            # Kiểm tra nếu số 1 có trong mảng
            nums.sort()  # Sắp xếp lại mảng
            for i in range(0, len(nums) - 1):
                # Duyệt qua từng phần tử của mảng
                if nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i]:
                    # Nếu số tiếp theo khác số hiện tại hoặc không tăng dần, ta đã tìm được số bị thiếu
                    if nums[i] + 1 > 0:
                        return nums[i] + 1  # Trả về số bị thiếu
            return nums[len(nums) - 1] + 1  # Nếu không có số bị thiếu trong khoảng từ 1 đến len(nums), trả về số lớn nhất + 1
        else:
            return 1  # Nếu không có số 1 trong mảng, số bị thiếu là 1
# @lc code=end

