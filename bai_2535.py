#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # Tính tổng các phần tử của mảng
        sum_nums = sum(nums)
        
        # Tính tổng các chữ số của từng phần tử trong mảng
        sum_digits = 0
        for num in nums:
            num_str = str(num)
            for digit in num_str:
                sum_digits += int(digit)
                
        # Tính hiệu tuyệt đối của tổng các phần tử và tổng các chữ số
        diff = abs(sum_nums - sum_digits)
        
        return diff
# @lc code=end

