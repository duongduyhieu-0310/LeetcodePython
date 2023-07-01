#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_products = [1] * n  # Mảng lưu tích lũy tích của phần tử bên trái nums[i]

        right_products = [1] * n  # Mảng lưu tích lũy tích của phần tử bên phải nums[i]

        for i in range(1, n):

            left_products[i] = left_products[i - 1] * nums[i - 1]  # Tích các phần tử bên trái nums[i]

        for i in range(n - 2, -1, -1):

            right_products[i] = right_products[i + 1] * nums[i + 1]  # Tích các phần tử bên phải nums[i]

        result = []

        for i in range(n):
            
            result.append(left_products[i] * right_products[i])  # Tích của các phần tử bên trái và bên phải

        return result



# @lc code=end

