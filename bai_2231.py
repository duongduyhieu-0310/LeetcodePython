#
# @lc app=leetcode id=2231 lang=python3
#
# [2231] Largest Number After Digit Swaps by Parity
#

# @lc code=start
class Solution:
    def largestInteger(self, num: int) -> int:
         a = list(str(num))
        b = []
        for i in a:
            b.append(int(i))

        c = []
        d = []
        for i in b:
            if i % 2 == 0:
                c.append(i)
            else:
                d.append(i)

        b_new = []
        for i in b:
            if i % 2 == 0:
                b_new.append(max(c))
                c.remove(max(c))
            else:
                b_new.append(max(d))
                d.remove(max(d))

        return int(''.join(map(str, b_new)))
        
# @lc code=end

