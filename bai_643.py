#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')  # Khởi tạo max_average với giá trị âm vô cùng
        
        # Tính tổng của k phần tử đầu tiên
        current_sum = sum(nums[:k])
        max_average = max(max_average, current_sum / k)
        
        for i in range(k, len(nums)):
            # Cập nhật tổng bằng cách thêm phần tử tiếp theo và trừ đi phần tử đầu tiên trong mảng con trước đó
            current_sum += nums[i] - nums[i - k]
            max_average = max(max_average, current_sum / k)
            
        return max_average
# @lc code=end

