#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
            result = 0
            n = len(arr)

            for a in range(1, n+1, 2):
                for i in range(n-a+1):
                    b = arr[i:i+a]
                    result += sum(b)

            return result



# @lc code=end

