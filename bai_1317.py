#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = []
        # Duyệt qua các giá trị của a từ 1 đến n/2
        for a in range(1, n // 2 + 1):
            # Tính giá trị tương ứng của b
            b = n - a
            # Kiểm tra xem a và b có chứa số 0 hay không
            if '0' not in str(a) and '0' not in str(b):
                ans.append(a)
                ans.append(b)
                break
        return ans

# @lc code=end

